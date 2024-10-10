from src.simulation.states.village import VillageState
from src.simulation.agents.village import VillageAgent
from src.simulation.entities.villager import Villager
from src.simulation.algorithms.genetic import genetic_algorithm
from src.simulation.actions.villager import VillagerAction
from src.simulation.actions.manager import ActionManager
from src.simulation.knowledge.knowledge import KnowledgeBase

class Village:
    def __init__(self, state=None, villagers=6):
        self.action_manager = ActionManager()
        self.state = VillageState(state)
        self.agent = VillageAgent(self.state)
        self.knowledge = KnowledgeBase()

        self.villagers = [Villager(f"Villager {i}") for i in range(villagers)]
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
            
    def execute_villager_task(self, villager: Villager, task: VillagerAction,i):
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
        return self.action_manager.predict_action(action, villager)
    
    def execute_action(self, action, villager):
        _, net_gain = self.action_manager.execute_action(
            action, 
            self, 
            villager,
            None # biome
        )      
        
        self.knowledge.update_village_knowledge(action.name, net_gain)

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
                value += predicted * knowledge # which percent of knowledge avg represents prediction

        return value
