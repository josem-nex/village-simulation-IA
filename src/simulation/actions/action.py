from actions.result import ACTION_RESULTS

class ActionChange:
    def __init__(self, village={}, villager={}):
        self._village = village
        self._villager = villager
        
    @property
    def village(self):
        return self._village
    
    @property
    def villager(self):
        return self._villager
    
class Action:
    def __init__(
        self, 
        name='',
        results=ACTION_RESULTS, 
        income: ActionChange=None, 
        outcome:ActionChange=None,
        need=''
    ):
        self._name = name
        self._need = need        
        self._results = results

        self._income = income or ActionChange()
        self._outcome = outcome or ActionChange()

    @property
    def name(self):
        return self._name

    @property
    def income(self):
        return self._income
    
    @property
    def outcome(self):
        return self._outcome
    
    @property
    def results(self):
        return self._results
    
    @property
    def need(self):
        return self._need
    
DailyVillagerChange = ActionChange(
    village={
        'food': 10,
        'water': 10,
        'wood': 0,
        'stone': 0,
        'herbs': 5,
        'metal': 0,
        'tools': 0
    },
    villager={
        'energy': -10,
        'hunger': -10,
        'thirst': -10,
        'mood': -10,
        'age': 1,
        'health': -5
    }
)
    