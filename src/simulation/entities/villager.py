import random
from math import log10

from src.simulation.states.villager import VillagerState
from src.simulation.agents.villager import VillagerAgent
from src.simulation.actions import villager as actions
from src.simulation.actions.village import VILLAGE_ACTIONS

class VillagerMastery:
    def __init__(self):
        self._mastery = {}

        for actions in VILLAGE_ACTIONS:
            self._mastery[actions.name] = 0

    def get_mastery(self, task):
        mastery = self._mastery[task.name]
        return 1 if mastery == 0 else int(log10(mastery))
    
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
class Villager(VillagerMastery):    
    def __init__(self, name):
        VillagerMastery.__init__(self)

        self.name = name
        self.state = VillagerState()
        self.agent = VillagerAgent(self.state)

    def select_task(self):
        self.agent.reset()
        self.agent.run()
        if len(self.agent.actions) == 0:
            self.agent.actions.append(actions.DefaultAction)
        return random.choice(self.agent.actions)

    def execute_task(self):
        print("Executing task...")