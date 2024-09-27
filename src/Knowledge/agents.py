from functools import reduce
from random import randint

class Resources:
    Food = "FOOD"
    Wood = "WOOD"
    Water = "WATER"

class Action:
    def __init__(self, duration, location, yields, events) -> None:
        self._duration = duration
        self._location = location
        self._yields = yields
        self._events = events
        
    @property
    def duration(self):
        return self._duration
    
    @property
    def location(self):
        return self._location
    
    @property
    def yields(self) -> dict[str, int]:
        return self._yields
    
    @property
    def events(self) -> list:
        return self._events
    
    # naive weight function
    @property
    def value(self) -> float:
        yields_val = reduce(lambda a, b: a + b, [x for x in self.yields.values()], 0)
        val = yields_val / self.duration
        success_prob = [x[1] for x in self.events if x[0] == "SUCCESS"]
        val *= success_prob[0] / 100
        
        return val

ACTIONS = {
    "FARM": Action(
        30, 
        "", 
        {
            Resources.Food: 300
        },
        [
            ("SUCCESS", 60)
        ]
    ),
    "HUNT": Action(
        7,
        "",
        {
            Resources.Food: 100
        },
        [
            ("SUCCESS", 40)
        ]
    ),
    "LUMBERJACK": Action(
        3,
        "",
        {
            Resources.Wood: 50
        },
        [
            ("SUCCESS", 80)
        ]
    ),
    # "BUILD": Action(
    # ),
    "BREED": Action(
        2,
        "",
        {},
        [
            ("SUCCESS", 10)
        ]
    ),
    "FIND_WATER": Action(
        1,
        "",
        {
            Resources.Water: 10
        },
        [
            ("SUCCESS", 90)
        ]
    )
}


class Village:
    def __init__(self):
        self._storage = {
            Resources.Food: 100,
            Resources.Wood: 50,
            Resources.Water: 100
        }

    @property
    def storage(self) -> dict[str, int]:
        return self._storage

class Villager:
    class Stats:
        Strength = "STR"
        Agility = "AGI"
        Intelligence = "INT"
        Stamina = "STA"
        Luck = "LUCK"

    def generate_random_stats() -> dict[str, int]:
        return {
            Villager.Stats.Strength: randint(1, 10),
            Villager.Stats.Agility: randint(1, 10),
            Villager.Stats.Intelligence: randint(1, 10),
            Villager.Stats.Stamina: randint(1, 10),
            Villager.Stats.Luck: randint(1, 10)
        }
    
    def __init__(self):
        self._stats = Villager.generate_random_stats()

    @property
    def stats(self) -> dict[str, int]:
        return self._stats
