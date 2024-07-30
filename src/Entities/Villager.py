

class Villager():
    def __init__(self, name, sex, age, health=100, hunger=0, skills={}, relationships={}):
        self.name = name
        self.sex = sex
        self.age = age
        self.health = health
        self.hunger = hunger
        self.job = None
        self.skills = skills
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
    
    def work(self):
        if self.job:
            self.job.perform_work(self)
        else:
            self.job = find_job()

    
    