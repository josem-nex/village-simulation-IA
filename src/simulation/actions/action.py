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
    def __init__(self, income: ActionChange = None, outcome:ActionChange=None, name='') -> None:
        self._name = name
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
    