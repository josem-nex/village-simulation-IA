from .action import Action, ActionChange

class VillagerAction(Action):
    pass

EatAction = VillagerAction(
    'eat',
    ActionChange(
        villager={
            'hunger': 20
        }
    ),
    ActionChange(
        village={
            'food': 10
        }
    )
)

SleepAction = VillagerAction(
    'sleep',
    ActionChange(
        villager={
            'energy': 60
        }
    )
)

NapAction = VillagerAction(
    'nap',
    ActionChange(
        villager={
            'energy': 15
        }
    )
)

DrinkAction = VillagerAction(
    'drink',
    ActionChange(
        villager={
            'thirst': 20
        }
    ),
    ActionChange(
        village={
            'water': 10
        }
    )
)

SocializeAction = VillagerAction(
    'socialize',
    ActionChange(
        villager={
            'mood': 15
        }
    ),
    ActionChange(
        villager={
            'energy': 10
        }
    )
)

VILLAGER_ACTIONS = [
    EatAction,
    SleepAction,
    NapAction,
    DrinkAction,
    SocializeAction
]
