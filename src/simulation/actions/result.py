from random import randint

class ActionResult:
    def __init__(self, positive=True, weight=1, income_modifier=1, outcome_modifier=1):
        self._positive = positive
        self._weight = weight
        self._income_modifier = income_modifier
        self._outcome_modifier = outcome_modifier

    @property
    def weight(self):
        return self._weight
    
    def get_modifier(self, income=True):
        return self._income_modifier if income else self._outcome_modifier
    
    def get_xp():
        return randint(0, 100)
    
    def is_positive(self):
        return self._positive

ActionResultSuccess = ActionResult(True, 1, 1, 1)
ActionResultLucky = ActionResult(True, 0.5, 1.5, 0.5)
ActionResultFailure = ActionResult(False, 1, 0, 1)
ActionResultDisaster = ActionResult(False, 0.5, 0, 1.5)

ACTION_RESULTS = [
    ActionResultSuccess,
    ActionResultFailure,
    ActionResultDisaster,
    ActionResultLucky
]