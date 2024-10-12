import random
from src.simulation.states.state import State


class VillageState(State):    
    def __init__(self, state=None):
        self._state = self.generate_random_state()
        if state is not None:
            for attribute in state:
                self._state[attribute] = state[attribute]

        self._fuzzy_functions = {
            'food': self.fuzzify_resource,
            'wood': self.fuzzify_resource,
            'stone': self.fuzzify_resource,
            'water': self.fuzzify_resource,
            'herbs': self.fuzzify_resource,
            'metal': self.fuzzify_resource,
            'tools': self.fuzzify_resource
        }    

    def generate_random_state(self):
        return {
            'food': random.randint(0, 100),
            'wood': random.randint(0, 100),
            'stone': random.randint(0, 100),
            'water': random.randint(0, 100),
            'herbs': random.randint(0, 100),
            'metal': random.randint(0, 100),
            'tools': random.randint(0, 100)
        }

    def get_attribute(self, attribute):
        return self.fuzzy_functions[attribute](attribute)
    
    def fuzzify_resource(self, resource):
        res = self.state[resource]
        if res < 5:
            return 'depleted'
        elif 10 <= res < 30:
            return 'low'
        elif 30 <= res < 70:
            return 'normal'
        else:
            return 'full'
