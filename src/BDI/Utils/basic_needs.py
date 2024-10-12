from typing import Dict, List
class BasicNeedTask:
    def __init__(self, name,active= True, duration=0, condition = None, cost = None, reward = None, consequences = None):
        self.name = name
        self.active = active
        self.duration = duration
        self.cost = cost or {}
        self.condition = condition or {}
        self.reward = reward or {}
        self.consequences = consequences or {}
        
    def __str__(self) -> str:
        return f'Task {self.name} with cost {self.cost} and reward {self.reward}'
    


eat = BasicNeedTask(name="Eat",
                    active=True,
                    cost={'food': 1},  # Cost of 1 unit of food
                    condition={'fullness': 0.6},  # Condition: fullness level must be below 0.6
                    reward={'fullness': 0.5, 'energy': 0.2, 'health':0.1},  # Reward: Reduces fullness, increases energy
                    consequences={'health':-0.1})  # In case of failure, health decreases
sleep = BasicNeedTask(name="Sleep",
                    active=False,
                    duration=8,  # Sleep for 8 hours
                    condition={'energy': 0.6},  # Condition: energy level must be below 0.6
                    reward={'energy': 0.5},  # Reward: Increases energy
                    consequences={'health': -0.2})       

drink = BasicNeedTask(name="Drink",
                    active=True,
                    cost={'water': 1},  # Cost of 1 unit of water
                    condition={'hydration': 0.7},  # Condition: Hydration level must be below 0.7
                    reward={'hydration': 0.4, 'energy': 0.1},  # Reward: Reduces hydration, increases energy    
                    consequences={'health': -0.1})  
rest = BasicNeedTask(name="Rest",
                    active=False,
                    duration=2,  # Rest for 2 hours
                    condition={'energy': 0.5},  # Condition: Health level must be below 0.6
                    reward={'health': 0.1, 'energy': 0.1},  # Reward: Increases health, increases energy
                    consequences={'health': -0.1})

idle = BasicNeedTask(name="Idle",
                    active=False,
                    duration=1,  # Do nothing for 1 hour
                    condition={},  # No condition
                    reward={'energy': 0.1,'fullness': -0.1, 'hydration':-0.1},  # Reward: Increases energy
                    consequences={})  # In case of failure, health decreases

death = BasicNeedTask(name="Death",
                    active=False,
                    duration=0,  # Instant death
                    condition={'health': 0.1},  # Condition: Health level must be 0
                    reward={})  # No reward


task: List[BasicNeedTask] = [idle, sleep, drink, rest, eat, death]