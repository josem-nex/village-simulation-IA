# from BDI.Entities.Villager import Villager
from typing import List

class Village:
    def __init__(self, name: str, villagers: List, resources = {}):
        self.name = name
        self.villagers = villagers
        self.resources = resources
        self.jobs = []
        
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def generate_tasks(self):
        tasks = []
        for villager in self.villagers:
            tasks.extend(villager.generate_tasks())
        return tasks
    
    def execute_tasks(self):
        for villager in self.villagers:
            tasks = villager.generate_tasks()
            villager.execute_task(self, tasks)
            
    def update(self):
        self.execute_tasks()
        for villager in self.villagers:
            villager.update()
            
    def get_villager(self, name: str):
        for villager in self.villagers:
            if villager.name == name:
                return villager
        return None
    
    def get_resource(self, name: str):
        return self.resources.get(name, None)
    
    def modify_resource(self, name: str, amount: int):
        if name in self.resources:
            self.resources[name] += amount
        else:
            self.resources[name] = amount