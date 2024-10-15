import random
from states.state import State
from actions.action import DailyVillagerChange


class VillageState(State):    
    def __init__(self, state=None, vilager_count=0):
        self.villager_count = vilager_count
        self._state = {}
        if state is not None:
            for attribute in state:
                self._state[attribute] = state[attribute]
        else:
            self._state = self.generate_random_state()

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
        # return {
        #     'food': random.randint(0, 100),
        #     'wood': random.randint(0, 100),
        #     'stone': random.randint(0, 100),
        #     'water': random.randint(0, 100),
        #     'herbs': random.randint(0, 100),
        #     'metal': random.randint(0, 100),
        #     'tools': random.randint(0, 100)
        # }
        return {
            'food': 50,
            'wood': 50,
            'stone': 50,
            'water': 50,
            'herbs': 50,
            'metal': 50,
            'tools': 50
        }
    
    def update_attribute(self, attribute, value):
        super().update_attribute(attribute, value)
        self._state[attribute] = max(0, self._state[attribute])

    def get_attribute(self, attribute):
        return self.fuzzy_functions[attribute](attribute)
    
    def fuzzify_resource(self, resource):
        # TODO res == 0 ? empty 
        res = self.state[resource]
        mult = 1 if self.villager_count == 0 else self.villager_count
        low_threshold = abs(DailyVillagerChange.village[resource])*mult
        if 0 < res < low_threshold:
            return 'depleted'
        elif low_threshold <= res < 3*low_threshold:
            return 'low'
        elif 3*low_threshold <= res < 7*low_threshold:
            return 'normal'
        else:
            return 'full'
