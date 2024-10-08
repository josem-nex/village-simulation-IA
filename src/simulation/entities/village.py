from ..states.village import VillageState
from ..agents.village import VillageAgent
from ..algorithms.genetic import genetic_algorithm
from ..knowledge.knowledge import KnowledgeBase
from .villager import Villager

class Village:
    def __init__(self, state=None):
        self.state = VillageState(state)
        self.agent = VillageAgent(self.state)
        self.knowledge = KnowledgeBase()
        self.villagers = [Villager(name=i) for i in range(2)]
        self.actions = []
        
    def add_villager(self, villager):
        self.villagers.append(villager)

    def remove_villager(self, villager):
        self.villagers.remove(villager)

    def get_villagers(self):
        return self.villagers
    
    def care_villagers(self):
        for i, villager in enumerate(self.villagers):
            print(f"Caring Villager {i}")
            villager.select_task()
    
    def infer_actions(self):
        self.agent.reset()
        self.agent.run()
        return self.agent.actions
    
    def predict_action_revenue(self, action, villager):
        return 1
    
    def execute_action(self, action, villager):
        result = 0

        for attribute in action.income.village:
            val = action.income.village[attribute]
            self.state.update_attribute(attribute, val)
            result += val
        for attribute in action.income.villager:
            val = action.income.villager[attribute]
            villager.state.update_attribute(attribute, val)
            result += val

        for attribute in action.outcome.village:
            val = action.outcome.village[attribute]
            self.state.update_attribute(attribute, -val)
            result -= val
        for attribute in action.outcome.villager:
            val = action.outcome.villager[attribute]
            villager.state.update_attribute(attribute, -val)
            result -= val
        
        self.knowledge.update_village_knowledge(action.name, result)

    def execute_actions(self, actions):
        for i, action in enumerate(actions):
            self.execute_action(action, self.villagers[i])
    
    def select_actions(self):
        best_sequence = genetic_algorithm(
            5, 
            len(self.villagers), 
            self.infer_actions(),
            lambda x: self.actions_fitness(x),
            0.6,
            5
        )
        print(
            [x.name for x in best_sequence[0] ]
        )

    def actions_fitness(self, actions):
        value = 0

        for i, action in enumerate(actions):
            # should wheight more or less depeding on the state changes
            # villager and village states
            # villager_state_copy = self.villagers[i].state

            predicted = self.predict_action_revenue(action, self.villagers[i])
            knowledge = self.knowledge.get_village_knowledge(action.name)
            
            if knowledge == 0:
                value += predicted
            else:
                value += predicted * 100 / knowledge # which percent of knowledge avg represents prediction

        return value
