from actions.action import Action, ActionChange


class VillagerTask(Action):
    pass

EatTask = VillagerTask(
    name='eat',
    income=ActionChange(
        villager={
            'hunger': 20
        }
    ),
    outcome=ActionChange(
        village={
            'food': -10
        }
    )
)

DrinkTask = VillagerTask(
    name='drink',
    income=ActionChange(
        villager={
            'thirst': 20
        }
    ),
    outcome=ActionChange(
        village={
            'water': -10
        }
    )
)

SleepTask = VillagerTask(
    name='sleep',
    income=ActionChange(
        villager={
            'energy': 50
        }
    )
)

HealTask = VillagerTask(
    name='heal',
    income=ActionChange(
        villager={
            'health': 20
        }
    ),
    outcome=ActionChange(
        village={
            'herbs': -10
        }
    )
)

NapTask = VillagerTask(
    name='nap',
    income=ActionChange(
        villager={
            'energy': 20
        }
    )
)

SocializeTask = VillagerTask(
    name='socialize',
    income=ActionChange(
        villager={
            'mood': 10
        }
    )
)

UnkownTask = VillagerTask(
    name='unknown',
    income=ActionChange(
        villager={
            'mood': -10
        }
    )
)