import random
from experta import KnowledgeEngine, Rule, Fact, Field, DefFacts, OR, AS, NOT, EXISTS, W

from actions import village as actions


VILLAGE_NEEDS = {
    'food': 10,
    'water': 10,
    'herbs': 10,
    'cook': 8,
    'stone': 7,
    'metal': 7,
    'wood': 7,
    'tools': 6,
}

class VillageFact(Fact):
    food = Field(str, default='')
    wood = Field(str, default='')
    water = Field(str, default='')
    stone = Field(str, default='')
    herbs = Field(str, default='')
    metal = Field(str, default='')
    tools = Field(str, default='')

class VillageNeed(Fact):
    need = Field(str, default='')

class Task:
    def __init__(self, name, incomes, outcomes) -> None:
        self.name = name
        self.incomes = incomes
        self.outcomes = outcomes

class VillageAgent(KnowledgeEngine):
    def __init__(self, state):
        super().__init__()
        self.state = state
        self.actions = []
        self.needs = []

    def reset(self, **kwargs):
        self.actions = []
        self.needs = []
        return super().reset(**kwargs)

    @DefFacts()
    def get_village_facts(self):
        state = {}
        for attribute in self.state.get_attributes():
            state[attribute] = self.state.get_attribute(attribute)
        print(state)
        yield VillageFact(**state)

    @Rule(OR(VillageFact(food='low'), VillageFact(food='depleted')), salience=VILLAGE_NEEDS['food'])
    def need_food(self):
        print("Village needs food.")
        self.declare(VillageNeed(need='food'))

    @Rule(VillageNeed(need='food'))
    def farm(self):
        # print("Village needs farming.")
        self.actions.append(actions.FarmAction)
        self.needs.append(10)

    @Rule(VillageNeed(need='food'))
    def gather_food(self):
        self.actions.append(actions.GatherFoodAction)
        self.needs.append(10)

    @Rule(OR(VillageFact(herbs='low'), VillageFact(herbs='depleted')), salience=VILLAGE_NEEDS['herbs'])
    def need_herbs(self):
        print("Village needs herbs.")
        self.declare(VillageNeed(need='herbs'))

    @Rule(VillageNeed(need='herbs'))
    def gather_herbs(self):
        # print("Village needs gathering herbs.")
        self.actions.append(actions.GatherHerbsAction)
        self.needs.append(10)

    @Rule(OR(VillageFact(water='low'), VillageFact(water='depleted')), salience=VILLAGE_NEEDS['water'])
    def need_water(self):
        print("Village needs water")
        self.declare(VillageNeed(need='water'))

    @Rule(VillageNeed(need='water'))
    def store_water(self):
        # print("Village needs storing water.")
        self.actions.append(actions.GatherWaterAction)
        self.needs.append(10)

    @Rule(VillageNeed(need='food'))
    def hunt(self):
        # print("Village needs hunting.")
        self.actions.append(actions.HuntAction)
        self.needs.append(10)

    # @Rule(OR(VillageNeed(need='food'))) # TODO: fix this by creating raw and consumable food
    # def cook(self):
    #     # print("Village needs cooking.")
    #     self.actions.append(actions.CookAction)

    @Rule(OR(VillageFact(tools='low'), VillageFact(tools='depleted')), salience=VILLAGE_NEEDS['tools'])
    def need_tools(self):
        print("Village needs tools")
        self.declare(VillageNeed(need='tools'))

    @Rule(VillageNeed(need='tools'))
    def forge(self):
        # print("Village needs forging.")
        self.actions.append(actions.ForgeAction)
        self.needs.append(1)

    @Rule(OR(VillageFact(metal='low'), VillageFact(metal='depleted')), salience=VILLAGE_NEEDS['metal'])
    def need_metal(self):
        print("Village needs metal")
        self.declare(VillageNeed(need='metal'))

    @Rule(OR(VillageNeed(need='metal'), VillageNeed(need='stone')))
    def mine(self):
        # print("Village needs mining.")
        self.actions.append(actions.MineAction)
        self.needs.append(1)

    @Rule(OR(VillageFact(stone='low'), VillageFact(stone='depleted')), salience=VILLAGE_NEEDS['stone'])
    def need_stone(self):
        print("Village needs stone")
        self.declare(VillageNeed(need='stone'))

    @Rule(VillageNeed(need='stone'))
    def gather_stone(self):
        # print("Village needs gathering stone.")  
        self.actions.append(actions.GatherStoneAction)
        self.needs.append(1)
        
    @Rule(OR(VillageFact(wood='low'), VillageFact(wood='depleted')), salience=VILLAGE_NEEDS['wood'])
    def need_wood(self):
        print("Village needs wood")
        self.declare(VillageNeed(need='wood'))
        self.needs.append(1)

    @Rule(VillageNeed(need='wood'))
    def chop_wood(self):
        # print("Village needs chopping wood.")
        self.actions.append(actions.ChopWoodAction)
        self.needs.append(1)

    @Rule(NOT(VillageNeed()))
    def no_needs(self):
        print(f"Village does not know what to do.")
        # print(fact.values())
        self.actions = actions.VILLAGE_ACTIONS       
        self.needs = [1 for _ in range(len(self.actions))]
        self.halt()
    

    # @Rule(Task(name='build'))
    # def build(self):
    #     print("Village needs building.")

    # @Rule(Task(name='repair'))
    # def repair(self):
    #     print("Village needs repairing.")

    # @Rule(Task(name='trade'))
    # def trade(self):
    #     print("Village needs trading.")

    # @Rule(Task(name='explore'))
    # def explore(self):
    #     print("Village needs exploring.")