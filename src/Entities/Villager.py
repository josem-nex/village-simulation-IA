

class Villager():
    def __init__(self, name, sex, age, health=100, hunger=0, skills={}, relationships={}):
        self.name = name
        self.sex = sex
        self.age = age
        self.health = health
        self.hunger = hunger
        self.energy = 1
        self.job = None
        self.skills = skills
        self.tools = []
        #  ? la cantidad de recursos/objetos que llevan encima 
        self.resources = {}
        #  ? las relaciones con otros aldeanos ?
        self.relationships = relationships
    
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def eat(self, food):
        self.hunger-= food.nutrition_value

    
    def add_skill(self, skill):
        self.skills.append(skill)
    
    def add_tool(self, tool):
        self.tools.append(tool)

    
    