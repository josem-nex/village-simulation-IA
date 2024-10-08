import random
from .state import State

class VillagerState(State):    
    def __init__(self):
        self._state = self.generate_random_state()
        self._fuzzy_functions = {
            'energy': self.fuzzify_energy,
            'hunger': self.fuzzify_hunger,
            'thirst': self.fuzzify_thirst,
            'health': self.fuzzify_health,
            'mood': self.fuzzify_mood,
            'age': self.fuzzify_age,
            'gender': self.fuzzify_gender,
        }    

    def apply_state_change(self, change):
        for attribute in change.villager:
            self.update_attribute(attribute, change.villager[attribute])

    def generate_random_state(self):
        return {
            'energy': random.randint(0, 100),
            'hunger': random.randint(0, 100),
            'thirst': random.randint(0, 100),
            'health': random.randint(0, 100),
            'mood': random.randint(0, 100),
            'age': random.randint(0, 100),
            'gender': random.randint(0, 1),
        }

    def fuzzify_energy(self):
        energy = self.state['energy']
        if energy < 10:
            return 'exhausted'
        elif 10 <= energy < 30:
            return 'tired'
        elif 30 <= energy < 70:
            return 'normal'
        else:
            return 'rested'

    def fuzzify_hunger(self):
        hunger = self.state['hunger']
        if hunger < 5:
            return 'starving'
        elif 5 <= hunger < 30:
            return 'hungry'
        elif 30 <= hunger < 70:
            return 'normal'
        else:
            return 'full'

    def fuzzify_thirst(self):
        thirst = self.state['thirst']
        if thirst < 5:
            return 'dehidrated'
        elif 5 <= thirst < 30:
            return 'thirsty'
        elif 30 <= thirst < 70:
            return 'normal'
        else:
            return 'full'

    def fuzzify_health(self):
        health = self.state['health']
        if health < 5:
            return 'sick'
        elif 5 <= health < 30:
            return 'injured'
        elif 30 <= health < 70:
            return 'average'
        else:
            return 'healthy'

    def fuzzify_mood(self):
        mood = self.state['mood']
        if mood < 30:
            return 'sad'
        elif 30 <= mood < 70:
            return 'neutral'
        else:
            return 'happy'

    def fuzzify_age(self):
        age = self.state['age']
        if age < 18:
            return 'child'
        elif 18 <= age < 55:
            return 'adult'
        else:
            return 'elder'

    def fuzzify_gender(self):
        gender = self.state['gender']
        if gender == 0:
            return 'male'
        else:
            return 'female'

