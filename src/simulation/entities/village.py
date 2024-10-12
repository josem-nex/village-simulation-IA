import random

from src.simulation.states.village import VillageState
from src.simulation.agents.village import VillageAgent, VILLAGE_NEEDS
from src.simulation.entities.villager import Villager
from src.simulation.algorithms.genetic import genetic_algorithm
from src.simulation.actions.villager import VillagerAction
from src.simulation.actions.manager import ActionManager
from src.simulation.knowledge.knowledge import KnowledgeBase
from src.simulation.actions.action import DailyVillagerChange

class Village:
    def __init__(self, state=None, villagers=6):
        self.action_manager = ActionManager(self)
        self.state = VillageState(state, villagers)
        self.agent = VillageAgent(self.state)
        self.knowledge = KnowledgeBase()

        self.villagers = [Villager(f"Villager {i}", self.action_manager) for i in range(villagers)]
        self.actions = []
        
    def add_villager(self, villager):
        self.villagers.append(villager)
        self.state.villager_count = self.state.villager_count + 1

    def remove_villager(self, villager):
        self.villagers.remove(villager)
        self.state.villager_count = self.state.villager_count - 1

    def get_villagers(self):
        return self.villagers
    
    def care_villagers(self):
        for i, villager in enumerate(self.villagers):
            # print(f"Caring Villager {i}")
            task = villager.select_task()
            # self.execute_villager_task(villager, task,i)
            
    def execute_villager_task(self, villager: Villager, task: VillagerAction,i):
        # print(f"Villager {i} is {task.name}")
        self.action_manager.execute_action(task, villager)
    
    def infer_actions(self):
        self.agent.reset()
        self.agent.run()
        return self.agent.actions
    
    def predict_action_revenue(self, action, villager):
        return self.action_manager.predict_action(action, villager)
    
    def execute_action(self, action, villager):
        _, net_gain = self.action_manager.execute_action(action, villager)              
        self.knowledge.update_village_knowledge(action.name, net_gain)

    def execute_actions(self, actions):
        for i, action in enumerate(actions):
            self.execute_action(action, self.villagers[i])
    
    def select_actions(self):
        if len(self.villagers) == 0:
            return []
        
        inferred_actions = self.infer_actions()

        if len(self.villagers) > 1:
            best_sequence = genetic_algorithm(
                5, 
                len(self.villagers), 
                inferred_actions,
                lambda x: self.actions_fitness(x),
                0.6,
                3
            )
        else:
            inferred_actions.sort(key=lambda x: VILLAGE_NEEDS[x.need], reverse=True)
            best_sequence = [[inferred_actions[0]]]
        
        print(
            [x.name for x in best_sequence[0] ]
        )
        return best_sequence[0]

    def actions_fitness(self, actions):
        value = 0

        for i, action in enumerate(actions):
            # should wheight more or less depeding on the state changes
            # villager and village states
            # villager_state_copy = self.villagers[i].state

            predicted = self.predict_action_revenue(action, self.villagers[i])
            knowledge = self.knowledge.get_village_knowledge(action.name)

            if not self.action_manager.can_execute_action(action, self.villagers[i]):
                predicted = 0
            
            if knowledge == 0:
                value += predicted * VILLAGE_NEEDS[action.need]
            else:
                value += predicted * knowledge * VILLAGE_NEEDS[action.need] # predicts if the action is going to be successfull

        return value
    
    def apply_daily_cost(self):
        daily_cost = DailyVillagerChange
        for villager in self.villagers:
            villager.state.apply_state_change(daily_cost)
    
    def check_villagers_status(self):
        for villager in self.villagers:
            villager.check_vital_signs()

            if 'DYING' in villager.status:
                print(f"Villager {villager.name} has died")
                villager.state.show_state()
                self.remove_villager(villager)
                continue

            if 'PREGNANT' in villager.status:
                print(f"Villager {villager.name} is pregnant")
                choices = [
                    'CHILD_LOST',
                    'KEEP_PREGNANCY',
                    'CHILD_BORN'
                ]
                wheigts = [
                    0.1 if villager.pregnancy_duration <= 7*30 else 0.05,
                    0.9 if villager.pregnancy_duration <= 7*30 else 0.15,
                    0.8 if villager.pregnancy_duration > 7*30 else 0
                ]
                result = random.choices(choices, wheigts)[0]

                if result == 'CHILD_LOST':
                    villager.status.remove('PREGNANT')
                    villager.pregnancy_duration = 0
                    villager.state.update_attribute('health', -25)
                elif result == 'KEEP_PREGNANCY':
                    continue
                elif result == 'CHILD_BORN':
                    villager.status.remove('PREGNANT')
                    villager.pregnancy_duration = 0
                    self.add_villager(Villager(f"Villager {len(self.villagers + 1)} was born"))
                    # print(f"Villager {villager.name} has given birth to a new villager")
                    
class VillageManager:
    def __init__(self, villagers=6):
        self.village = Village(villagers=villagers)
