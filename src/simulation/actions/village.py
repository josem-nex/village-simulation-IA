from actions.action import Action, ActionChange

class VillageAction(Action):
    pass

FarmAction = VillageAction(
    name='farm', 
    income=ActionChange(
        village={
            'food': 10
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 40
        }
    )
)

GatherHerbsAction = VillageAction(
    name='gather_herbs',
    income=ActionChange(
        village={
            'herbs': 5
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 35
        }
    )
)

GatherWaterAction = VillageAction(
    name='gather_water',
    income=ActionChange(
        village={
            'water': 8
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 20
        }
    )
)

CookAction = VillageAction(
    name='cook',
    income=ActionChange(
        village={
            'food': 10
        }
    ),
    outcome=ActionChange(
        village={
            'food': 20
        },
        villager={
            'energy': 15,
        }
    )
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
            'tools': 2
        },
        villager={
            'energy': 60,            
        }
    )
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
            'energy': 55
        }
    )
)

MineAction = VillageAction(
    name='mine',
    income=ActionChange(
        village={
            'metal': 5,
            'stone': 15
        }
    ),
    outcome=ActionChange(
        village={
            'tools': 3
        },
        villager={
            'energy': 60
        }
    )
)

GatherStoneAction = VillageAction(
    name='gather_stone',
    income=ActionChange(
        village={
            'stone': 10
        }
    ),
    outcome=ActionChange(
        village={
            'tools': 2
        },
        villager={
            'energy': 40
        }
    )
)

ChopWoodAction = VillageAction(
    name='chop_wood',
    income=ActionChange(
        village={
            'wood': 15
        }
    ),
    outcome=ActionChange(
        village={
            'tools': 2
        },
        villager={
            'energy': 50
        }
    )
)



VILLAGE_ACTIONS = [
    FarmAction,
    GatherHerbsAction,
    GatherWaterAction,
    CookAction,
    HuntAction,
    ForgeAction,
    MineAction,
    GatherStoneAction
]