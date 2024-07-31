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
    def yields(self):
        return self._yields
    
    @property
    def events(self):
        return self._events

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
