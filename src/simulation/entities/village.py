from states.village import VillageState
from agents.village import VillageAgent
from entities.villager import Villager
from algorithms.genetic import genetic_algorithm

class Village:
    def __init__(self, state=None):
        self.state = VillageState(state)
        self.agent = VillageAgent(self.state)
        self.villagers = [Villager() for _ in range(6)]
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
        village_state_copy = self.state
        value = 0

        for i, action in enumerate(actions):
            # should wheight more or less depeding on the state changes
            # villager and village states
            villager_state_copy = self.villagers[i].state

            for attribute in action.income.village:
                val = action.income.village[attribute]
                village_state_copy.update_attribute(attribute, val)
                value += val
            for attribute in action.income.villager:
                val = action.income.villager[attribute]
                villager_state_copy.update_attribute(attribute, val)
                value += val

            for attribute in action.outcome.village:
                val = action.outcome.village[attribute]
                village_state_copy.update_attribute(attribute, -val)
                value -= val
            for attribute in action.outcome.villager:
                val = action.outcome.villager[attribute]
                villager_state_copy.update_attribute(attribute, -val)
                value -= val

        return value
