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
    def __init__(self, name='', income={}, outcome={}) -> None:
        self._name = name
        self._income = income
        self._outcome = outcome

    @property
    def name(self):
        return self._name

    @property
    def income(self):
        return self._income
    
    @property
    def outcome(self):
        return self._outcome
    