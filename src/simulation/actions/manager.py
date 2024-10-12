import random
from src.simulation.actions.village import VillageAction

class ActionManager:
    def __init__(self, village, biome=None):
        self.village=village
        self.biome=biome

    def can_execute_action(self, action, villager):
        for attribute in action.outcome.village:
            val = action.outcome.village[attribute]
            if self.village.state.get_attribute_value(attribute) < val:
                return False
            
        for attribute in action.outcome.villager:
            val = action.outcome.villager[attribute]
            if villager.state.get_attribute_value(attribute) < val:
                return False

        return True

    def execute_action(self, action, villager):
        if isinstance(action, VillageAction):
            mastery = villager.get_mastery(action)
            weighted_mastery = [mastery * result.weight if result.is_positive() else 1 / mastery * result.weight for result in action.results]
            result = random.choices(action.results, weighted_mastery)[0]
        else:
            result = random.choices(action.results, [result.weight for result in action.results])[0]
        net_gain = 0

        income_mod = result.get_modifier()
        outcome_mod = result.get_modifier(False)

        for attribute in action.income.village:
            val = action.income.village[attribute] * income_mod
            self.village.state.update_attribute(attribute, val)
            net_gain += val
        
        for attribute in action.income.villager:
            val = action.income.villager[attribute] * income_mod
            villager.state.update_attribute(attribute, val) 

        for attribute in action.outcome.village:
            val = action.outcome.village[attribute] * outcome_mod
            self.village.state.update_attribute(attribute, -val)
            net_gain -= val

        for attribute in action.outcome.villager:
            val = action.outcome.villager[attribute] * outcome_mod
            villager.state.update_attribute(attribute, -val)

        if isinstance(action, VillageAction):
            villager.update_mastery(action, result.get_xp())
        
        return result, net_gain


    def predict_action(self, action, villager):
        mastery = villager.get_mastery(action)
        weighted_mastery = [mastery * result.weight if result.is_positive() else 1 / mastery * result.weight for result in action.results]
        result = random.choices(action.results, weighted_mastery)[0]

        return 1 if result.is_positive() else -1
    