from experta import KnowledgeEngine, Rule, Fact, Field, DefFacts, OR, AS, L
from actions import villager as actions
from states.villager import VillagerState
class Task(Fact):
    name = Field(str, default='')
    energy = Field(int, default='')
    hunger = Field(int, default='')
    thirst = Field(int, default='')
    health = Field(int, default='')
    mood = Field(int, default='')
    age = Field(int, default='')
    gender = Field(int, default='')

class VillagerFact(Fact):
    name= Field(str, default='')
    energy = Field(str, default='')
    hunger = Field(str, default='')
    thirst = Field(str, default='')
    health = Field(str, default='')
    mood = Field(str, default='')
    age = Field(str, default='')

class VillagerAgent(KnowledgeEngine):
    def __init__(self, state: VillagerState):
        super().__init__()
        self.state = state
        self.actions = []

    @DefFacts()
    def get_villager_facts(self):
        state = {}
        for attribute in self.state.get_attributes():
            state[attribute] = self.state.get_attribute(attribute)
        yield VillagerFact(**state)
    
    # personal tasks
    @Rule(OR(VillagerFact(hunger='hungry')) , VillagerFact(hunger='starving'))
    def eat(self):
        # print("Villager need eating.")
        # self.declare(Task(name='eat'))
        self.actions.append(actions.EatTask)

    @Rule(VillagerFact(energy='exhausted'))
    def sleep(self):
        # print("Villager  sleeping.")
        # self.declare(Task(name='sleep'))
        self.actions.append(actions.SleepTask)

    @Rule(VillagerFact(energy='tired'))
    def nap(self):
        # print("Villager is taking a nap.")
        # self.declare(Task(name='nap'))
        self.actions.append(actions.NapTask)

    @Rule(OR(VillagerFact(thirst='thirsty'), VillagerFact(thirst='dehidrated')))
    def drink(self):
        # print("Villager is drinking water.")
        # self.declare(Task(name='drink'))
        self.actions.append(actions.DrinkTask)

    @Rule(OR(VillagerFact(mood='sad'), VillagerFact(mood='neutral')))
    def socialize(self):
        # print("Villager is socializing.")
        # self.declare(Task(name='socialize'))
        self.actions.append(actions.SocializeTask)
        
    @Rule(AS.fact << Fact())
    def unknown_task(self, fact):
        # print(f"Villager does not know what to do.")
        # print(fact.values())
        self.actions.append(actions.UnknownTask)


