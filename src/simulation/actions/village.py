from .action import Action, ActionChange

class VillageAction(Action):
    pass

FarmAction = VillageAction(
    'farm', 
    ActionChange(
        village={
            'food': 10
        }
    ),
    ActionChange(
        villager={
            'energy': 40
        }
    )
)

GatherHerbsAction = VillageAction(
    'gather_herbs',
    ActionChange(
        village={
            'herbs': 5
        }
    ),
    ActionChange(
        villager={
            'energy': 35
        }
    )
)

GatherWaterAction = VillageAction(
    'gather_water',
    ActionChange(
        village={
            'water': 8
        }
    ),
    ActionChange(
        villager={
            'energy': 20
        }
    )
)

CookAction = VillageAction(
    'cook',
    ActionChange(
        village={
            'food': 10
        }
    ),
    ActionChange(
        village={
            'food': 20
        },
        villager={
            'energy': 15,
        }
    )
)

HuntAction = VillageAction(
    'hunt',
    ActionChange(
        village={
            'food': 15,
        }
    ),
    ActionChange(
        village={
            'tools': 2
        },
        villager={
            'energy': 60,            
        }
    )
)

ForgeAction = VillageAction(
    'forge',
    ActionChange(
        village={
            'tools': 5
        }
    ),
    ActionChange(
        village={
            'metal': 25
        },
        villager={
            'energy': 55
        }
    )
)

MineAction = VillageAction(
    'mine',
    ActionChange(
        village={
            'metal': 5,
            'stone': 15
        }
    ),
    ActionChange(
        village={
            'tools': 3
        },
        villager={
            'energy': 60
        }
    )
)

GatherStoneAction = VillageAction(
    'gather_stone',
    ActionChange(
        village={
            'stone': 10
        }
    ),
    ActionChange(
        village={
            'tools': 2
        },
        villager={
            'energy': 40
        }
    )
)
