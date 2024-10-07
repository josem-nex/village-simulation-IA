from states.villager import VillagerState
from agents.villager import VillagerAgent
from actions import villager as actions

import random
class Villager:    
    def __init__(self):
        self.state = VillagerState()
        self.agent = VillagerAgent(self.state)

    def select_task(self):
        self.agent.reset()
        self.agent.run()
        if len(self.agent.actions) == 0:
            self.agent.actions.append(actions.UnkownTask)
        return random.choice(self.agent.actions)

    def execute_task(self):
        print("Executing task...")