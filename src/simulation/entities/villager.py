from states.villager import VillagerState
from agents.villager import VillagerAgent
class Villager:    
    def __init__(self):
        self.state = VillagerState()
        self.agent = VillagerAgent(self.state)

    def select_task(self):
        self.agent.reset()
        self.agent.run()

    def execute_task(self):
        print("Executing task...")