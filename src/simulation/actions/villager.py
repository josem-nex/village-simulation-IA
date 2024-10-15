from actions.action import Action, ActionChange

class VillagerAction(Action):
    pass

EatAction = VillagerAction(
    'eat',
    income=ActionChange(
        villager={
            'hunger': 30
        }
    ),
    outcome=ActionChange(
        village={
            'food': 15
        }
    )
)

SleepAction = VillagerAction(
    'sleep',
    income=ActionChange(
        villager={
            'energy': 60
        }
    )
)

NapAction = VillagerAction(
    'nap',
    income=ActionChange(
        villager={
            'energy': 15
        }
    )
)

DrinkAction = VillagerAction(
    'drink',
    income=ActionChange(
        villager={
            'thirst': 30
        }
    ),
    outcome=ActionChange(
        village={
            'water': 15
        }
    )
)

SocializeAction = VillagerAction(
    'socialize',
    income=ActionChange(
        villager={
            'mood': 15
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 30
        }
    )
)

GetPregnantAction = VillagerAction(
    'get_pregnant',
    income=ActionChange(
        villager={
            'mood': 15
        }
    ),
    outcome=ActionChange(
        villager={
            'energy': 30,
        }
    )
)

DefaultAction = VillagerAction(
    'do_nothing'
)

VILLAGER_ACTIONS = [
    EatAction,
    SleepAction,
    NapAction,
    DrinkAction,
    SocializeAction,
    DefaultAction
]
