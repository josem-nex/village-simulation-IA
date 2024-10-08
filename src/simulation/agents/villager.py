from experta import KnowledgeEngine, Rule, Fact, Field, DefFacts, OR, AS, L

from ..states.villager import VillagerState
from ..actions import villager as actions

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

# define task cost in energy
# define task outcomes
# define task incomes
# define task requirements
# define task dependencies
class VillagerAgent(KnowledgeEngine):
    def __init__(self, state: VillagerState):
        super().__init__()
        self.state = state

    @DefFacts()
    def get_villager_facts(self):
        state = {}
        for attribute in self.state.get_attributes():
            state[attribute] = self.state.get_attribute(attribute)
        yield VillagerFact(**state)
    
    @Rule(AS.fact << VillagerFact(), OR(VillagerFact(hunger='hungry')) , VillagerFact(hunger='starving'))
    def eat(self, fact):
        print("Villager is eating.")
        self.state.apply_state_change(actions.EatAction.income)
        self.state.apply_state_change(actions.EatAction.outcome)
        self.retract(fact)
        for x in self.get_villager_facts():
            self.declare(x)

        # self.state.show_state()
        

    @Rule(AS.fact << VillagerFact(), VillagerFact(energy='exhausted'))
    def sleep(self, fact):
        print("Villager is sleeping.")
        self.state.apply_state_change(actions.SleepAction.income)
        self.state.apply_state_change(actions.SleepAction.outcome)
        self.retract(fact)
        for x in self.get_villager_facts():
            self.declare(x)
        
        # self.state.show_state()


    @Rule(AS.fact << VillagerFact(), VillagerFact(energy='tired'))
    def nap(self, fact):
        print("Villager is taking a nap.")
        self.state.apply_state_change(actions.NapAction.income)
        self.state.apply_state_change(actions.NapAction.outcome)
        self.retract(fact)
        for x in self.get_villager_facts():
            self.declare(x)

        # self.state.show_state()        

    @Rule(AS.fact << VillagerFact(), OR(VillagerFact(thirst='thirsty'), VillagerFact(thirst='dehidrated')))
    def drink(self, fact):
        print("Villager is drinking water.")
        self.state.apply_state_change(actions.DrinkAction.income)
        self.state.apply_state_change(actions.DrinkAction.outcome)
        self.retract(fact)
        for x in self.get_villager_facts():
            self.declare(x)

        # self.state.show_state()

    @Rule(AS.fact << VillagerFact(), VillagerFact(mood='sad'))
    def socialize(self, fact):
        print("Villager is socializing.")
        self.state.apply_state_change(actions.SocializeAction.income)
        self.state.apply_state_change(actions.SocializeAction.outcome)
        self.retract(fact)
        for x in self.get_villager_facts():
            self.declare(x)

        # self.state.show_state()
        
    @Rule(AS.fact << Fact())
    def unknown_task(self, fact):
        print(f"Villager does not know what to do.")
        # print(fact.values())


