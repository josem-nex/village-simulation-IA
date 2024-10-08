from states.village import VillageState
from agents.village import VillageAgent
from entities.villager import Villager
from algorithms.genetic import genetic_algorithm
from actions.villager import VillagerTask

class Village:
    def __init__(self, state=None, villagers=6):
        self.state = VillageState(state)
        self.agent = VillageAgent(self.state)
        self.villagers = [Villager() for _ in range(villagers)]
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
            task = villager.select_task()
            self.execute_villager_task(villager, task,i)
            
    def execute_villager_task(self, villager: Villager, task: VillagerTask,i):
        print(f"Villager {i} is {task.name}")
        for income in task.income.village:
            val = task.income.village[income]
            self.state.update_attribute(income, val)
        for income in task.income.villager:
            val = task.income.villager[income]
            villager.state.update_attribute(income, val)
        for outcome in task.outcome.village:
            val = task.outcome.village[outcome]
            self.state.update_attribute(outcome, val)
        for outcome in task.outcome.villager:
            val = task.outcome.villager[outcome]
            villager.state.update_attribute(outcome, val) 
    
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
