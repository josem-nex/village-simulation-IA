import random
from experta import KnowledgeEngine, Rule, Fact, Field, DefFacts, OR, AS, L

from actions import village as actions

class VillageFact(Fact):
    food = Field(str, default='')
    wood = Field(str, default='')
    water = Field(str, default='')
    stone = Field(str, default='')
    herbs = Field(str, default='')
    metal = Field(str, default='')
    tools = Field(str, default='')

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

    def reset(self, **kwargs):
        self.actions = []
        return super().reset(**kwargs)

    @DefFacts()
    def get_village_facts(self):
        state = {}
        for attribute in self.state.get_attributes():
            state[attribute] = self.state.get_attribute(attribute)
        yield VillageFact(**state)

    @Rule(OR(VillageFact(food='low'), VillageFact(food='depleted')))
    def farm(self):
        print("Village needs farming.")
        self.actions.append(actions.FarmAction)

    @Rule(OR(VillageFact(herbs='low'), VillageFact(herbs='depleted')))
    def gather_herbs(self):
        print("Village needs gathering herbs.")
        self.actions.append(actions.GatherHerbsAction)

    @Rule(OR(VillageFact(water='low'), VillageFact(water='depleted')))
    def store_water(self):
        print("Village needs storing water.")
        self.actions.append(actions.GatherWaterAction)

    @Rule(OR(VillageFact(food='low'), VillageFact(food='depleted')))
    def hunt(self):
        print("Village needs hunting.")
        self.actions.append(actions.HuntAction)

    @Rule(OR(VillageFact(food='low'), VillageFact(food='depleted')))
    def cook(self):
        print("Village needs cooking.")
        self.actions.append(actions.CookAction)

    @Rule(OR(VillageFact(tools='low'), VillageFact(tools='depleted')))
    def forge(self):
        print("Village needs forging.")
        self.actions.append(actions.ForgeAction)

    @Rule(OR(VillageFact(metal='low'), VillageFact(metal='depleted')))
    def mine(self):
        print("Village needs mining.")
        self.actions.append(actions.MineAction)

    @Rule(OR(VillageFact(metal='low'), VillageFact(metal='depleted')))
    def gather_stone(self):
        print("Village needs gathering stone.")  
        self.actions.append(actions.GatherStoneAction)  
        
    @Rule(OR(VillageFact(wood='low'), VillageFact(wood='depleted')))
    def chop_wood(self):
        print("Village needs chopping wood.")
        self.actions.append(actions.ChopWoodAction)
        
    

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