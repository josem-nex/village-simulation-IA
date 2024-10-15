import random
from math import log10

from states.villager import VillagerState
from agents.villager import VillagerAgent
from actions import villager as actions
from actions.village import VILLAGE_ACTIONS


VILLAGER_STATUS = [
    'DYING',
    'PREGNANT',
    'TIRED'
]

class VillagerMastery:
    def __init__(self):
        self._mastery = {}

        for actions in VILLAGE_ACTIONS:
            self._mastery[actions.name] = 10

    def get_mastery(self, task):
        mastery = self._mastery[task.name]
        return int(log10(mastery))
    
    def get_mastery_level(self, task):
        mastery = self.get_mastery(task)

        if mastery < 1:
            return "novice"
        elif 1 <= mastery < 3:
            return "apprentice"
        elif 3 <= mastery < 5:
            return "artisan"
        
        return "expert"
    
    def update_mastery(self, task, value):
        self._mastery[task.name] += value

class VillagerPregnancy:
    def __init__(self):
        self._duration = 0

    @property
    def pregnancy_duration(self):
        return self._duration
    
    def update_pregnancy(self):
        self._duration += 1

class Villager(VillagerMastery, VillagerPregnancy):    
    def __init__(self, name, manager):
        VillagerMastery.__init__(self)
        VillagerPregnancy.__init__(self)

        self.status = ['NORMAL']
        self.name = name
        self.state = VillagerState()
        self.agent = VillagerAgent(self, manager)

    def check_vital_signs(self):
        # reset statuses
        self.status = []
        age_die_prob = 0

        if self.state.get_attribute('age') == 'elder':
            age_die_prob = random.randint(0, 100)

        if self.state.get_attribute('energy') == 'exhausted':
            self.status.append('TIRED')
        
        if self.state.get_attribute('health') == 'sick' or \
            self.state.get_attribute('hunger') == 'starving' or \
            self.state.get_attribute('thirst') == 'dehydrated' or \
            age_die_prob >= 95:
            self.status.append('DYING')
        
    def select_task(self):
        self.agent.reset()
        self.agent.run()
        # if len(self.agent.actions) == 0:
        #     self.agent.actions.append(actions.DefaultAction)
        # # selection = random.choice(self.agent.actions)
        # selection = self.agent.actions[0]

        # if selection.name == 'get_pregnant':
        #     self.status.append('PREGNANT')
                               
        # return selection

    def execute_task(self):
        print("Executing task...")
 