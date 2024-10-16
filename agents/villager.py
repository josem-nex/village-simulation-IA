from experta import KnowledgeEngine, Rule, Fact, Field, DefFacts, OR, AS, AND, NOT, L
from actions import villager as actions
from actions.manager import ActionManager
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
    gender = Field(str, default='')

class VillagerNeed(Fact):
    need = Field(str, default='')

class VillagerAgent(KnowledgeEngine):
    def __init__(self, villager, manager: ActionManager):
        super().__init__()
        self.villager = villager
        self.actions = []
        self.manager = manager

    @DefFacts()
    def get_villager_facts(self):
        state = {}
        for attribute in self.villager.state.get_attributes():
            state[attribute] = self.villager.state.get_attribute(attribute)
        yield VillagerFact(**state)

    # TODO: add needs as facts redefinition and then execute tasks given those needs
    
    # personal tasks

    @Rule(OR(VillagerFact(health='injured'), VillagerFact(health='sick')))
    def need_heal(self):
        self.declare(VillagerNeed(need='health'))

    @Rule(OR(VillagerFact(hunger='hungry'), VillagerFact(hunger='starving')))
    def need_food(self):
        self.declare(VillagerNeed(need='hunger'))
    
    @Rule(OR(VillagerFact(thirst='thirsty'), VillagerFact(thirst='dehidrated')))
    def need_water(self):
        self.declare(VillagerNeed(need='thirst'))

    @Rule(OR(VillagerFact(mood='sad'), VillagerFact(mood='neutral')))
    def need_socialize(self):
        self.declare(VillagerNeed(need='mood'))

    @Rule(OR(VillagerFact(energy='exhausted'), VillagerFact(energy='tired')))
    def need_sleep(self):
        self.declare(VillagerNeed(need='sleep'))

    @Rule(VillagerNeed(need='health'), salience=10)
    def heal(self):
        # self.declare(Task(name='heal'))
        if self.manager.can_execute_action(actions.HealAction, self.villager):
            print("Villager is healing.")
            self.manager.execute_action(actions.HealAction, self.villager)
            # self.reset()

    @Rule(VillagerNeed(need='hunger'), salience=10)
    def eat(self):
        # TODO: villager is not eating
        # self.declare(Task(name='eat'))
        print("Villager need eating.")
        if self.manager.can_execute_action(actions.EatAction, self.villager):
            print("villager is eating")
            self.manager.execute_action(actions.EatAction, self.villager)
            # self.reset() #TODO: avoid use reset

    @Rule(VillagerNeed(need='sleep'), salience=9)
    def sleep(self):
        print("Villager  sleeping.")
        # self.declare(Task(name='sleep'))
        if self.manager.can_execute_action(actions.EatAction, self.villager):
            self.manager.execute_action(actions.SleepAction, self.villager)
            # self.reset()

    @Rule(VillagerNeed(need='sleep'), salience=8)
    def nap(self):
        # self.declare(Task(name='nap'))
        if self.manager.can_execute_action(actions.NapAction, self.villager):
            print("Villager is taking a nap.")
            self.manager.execute_action(actions.NapAction, self.villager)
            # self.reset()

    @Rule(VillagerNeed(need='thirst'), salience=10)
    def drink(self):
        # self.declare(Task(name='drink'))
        if self.manager.can_execute_action(actions.DrinkAction, self.villager):
            print("Villager is drinking water.")
            self.manager.execute_action(actions.DrinkAction, self.villager)
            # self.reset()

    @Rule(VillagerNeed(need='mood'), salience=8)
    def socialize(self):
        # self.declare(Task(name='socialize'))
        if self.manager.can_execute_action(actions.SocializeAction, self.villager):
            print("Villager is socializing.")
            self.manager.execute_action(actions.SocializeAction, self.villager)
            # self.reset()

    @Rule(AND(NOT(VillagerFact(age='child')), NOT(VillagerFact(age='elder')), VillagerFact(mood='happy'), VillagerFact(sex='female')), salience=7)
    def get_pregnant(self):
        if self.manager.can_execute_action(actions.GetPregnantAction, self.villager):
            self.manager.execute_action(actions.GetPregnantAction, self.villager)
            self.villager.status.append('PREGNANT')
            # self.reset()
                
    # @Rule(AS.fact << Fact())
    # def unknown_task(self, fact):
    #     print(f"Villager does not know what to do.")
    #     # print(fact.values())
    #     self.manager.execute_action(actions.DefaultAction, self.villager)


