import random

MAX_MASTERY_LEVEL = 10

class ActionManager:
    def execute_action(self, action, village, villager, biome):
        mastery = villager.get_mastery(action)
        weighted_mastery = [mastery * result.weight if result.is_positive() else 1 / mastery * result.weight for result in action.results]
        result = random.choices(action.results, weighted_mastery)[0]
        net_gain = 0

        income_mod = result.get_modifier()
        outcome_mod = result.get_modifier(False)

        for attribute in action.income.village:
            val = action.income.village[attribute] * income_mod
            village.state.update_attribute(attribute, val)
            net_gain += val
        
        for attribute in action.income.villager:
            val = action.income.villager[attribute] * income_mod
            villager.state.update_attribute(attribute, val) 

        for attribute in action.outcome.village:
            val = action.outcome.village[attribute] * outcome_mod
            village.state.update_attribute(attribute, -val)
            net_gain -= val

        for attribute in action.outcome.villager:
            val = action.outcome.villager[attribute] * outcome_mod
            villager.state.update_attribute(attribute, -val)

        villager.update_mastery(action, result.get_xp())
    
    def predict_action(self, action, villager):
        mastery = villager.get_mastery(action)
        weighted_mastery = [mastery * result.weight if result.is_positive() else 1 / mastery * result.weight for result in action.results]
        result = random.choices(action.results, weighted_mastery)[0]

        return 1 if result.is_positive() else -1
    