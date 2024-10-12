from src.simulation.actions.action import Action, ActionChange

class VillageAction(Action):
    pass

FarmAction = VillageAction(
    name='farm', 
    income=ActionChange(
        village={
            'food': 15
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 30
        }
    ),
    need='food'
)

GatherHerbsAction = VillageAction(
    name='gather_herbs',
    income=ActionChange(
        village={
            'herbs': 8
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 40
        }
    ),
    need='herbs'
)

GatherFoodAction = VillageAction(
    name='gather_food',
    income=ActionChange(
        village={
            'food': 10
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 30
        }
    ),
    need='food'
)

GatherWaterAction = VillageAction(
    name='gather_water',
    income=ActionChange(
        village={
            'water': 15
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 30
        }
    ),
    need='water'
)

# TODO: fix this with raw and cooked food
CookAction = VillageAction(
    name='cook',
    income=ActionChange(
        village={
            'food': 20
        }
    ),
    outcome=ActionChange(
        village={
            'food': 20
        },
        villager={
            'energy':20,
        }
    ),
    need='food'
)

HuntAction = VillageAction(
    name='hunt',
    income=ActionChange(
        village={
            'food': 15,
        }
    ),
    outcome=ActionChange(
        village={
            'tools': 4
        },
        villager={
            'energy': 60,            
        }
    ),
    need='food'
)

ForgeAction = VillageAction(
    name='forge',
    income=ActionChange(
        village={
            'tools': 5
        }
    ),
    outcome=ActionChange(
        village={
            'metal': 25
        },
        villager={
            'energy': 60
        }
    ),
    need='tools'
)

MineAction = VillageAction(
    name='mine',
    income=ActionChange(
        village={
            'metal': 5,
            'stone': 10
        }
    ),
    outcome=ActionChange(
        village={
            'tools': 4
        },
        villager={
            'energy': 60
        }
    ),
    need='metal'
)

GatherStoneAction = VillageAction(
    name='gather_stone',
    income=ActionChange(
        village={
            'stone': 7
        }
    ),
    outcome=ActionChange(
        village={
            'tools': 3
        },
        villager={
            'energy': 45
        }
    ),
    need='stone'
)

ChopWoodAction = VillageAction(
    name='chop_wood',
    income=ActionChange(
        village={
            'wood': 7
        }
    ),
    outcome=ActionChange(
        village={
            'tools': 3
        },
        villager={
            'energy': 50
        }
    ),
    need='wood'
)

VILLAGE_ACTIONS = [
    FarmAction,
    GatherHerbsAction,
    GatherFoodAction,
    GatherWaterAction,
    CookAction,
    HuntAction,
    ForgeAction,
    MineAction,
    GatherStoneAction
]