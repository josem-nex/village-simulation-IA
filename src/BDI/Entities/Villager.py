from BDI.Utils.basic_needs import task, BasicNeedTask
from BDI.Entities.Village import Village
import random
from typing import List


class Villager():
    def __init__(self, name, sex, age, health=1, fullness=1, hydration=1, energy=1):
        self.name = name
        self.sex = sex
        self.age = age
        self.job = None
        self._active = True
        
        self.beliefs = {
            "health": health,
            "fullness": fullness,
            "hydration": hydration,
            "energy": energy,
            # "skills": {},
            "village_job": None,
            "basic_needs": None
        }
        
        self.desires = {
            "health": 1,
            "fullness": 1,
            "energy": 1,
            "hydration": 1,
            "finish_village_job": False,
            "finish_basic_needs": True
        }

    def fullness(self) -> str:
        if self.beliefs["fullness"] < 0.3:
            return "starving"
        elif self.beliefs["fullness"] < 0.6:
            return "hungry"
        else:
            return "full"
        
    def hydration(self) -> str:
        if self.beliefs["hydration"] < 0.3:
            return "dehydrated"
        elif self.beliefs["hydration"] < 0.6:
            return "thirsty"
        else:
            return "hydrated"
        
    def energy(self) -> str:
        if self.beliefs["energy"] < 0.3:
            return "exhausted"
        elif self.beliefs["energy"] < 0.6:
            return "tired"
        else:
            return "energetic"
        
    def health(self) -> str:
        if self.beliefs["health"] < 0.3:
            return "dying"
        elif self.beliefs["health"] < 0.6:
            return "sick"
        else:
            return "healthy"
    
    def check_beliefs(self):
        for k, v in self.beliefs.items():
            if v:
                if v < 0:
                    self.beliefs[k] = 0
                elif v > 1:
                    self.beliefs[k] = 1
    
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def generate_tasks(self):
        tasks = []
        if self.desires["finish_basic_needs"]:
            for t in task:
                for k, v in t.condition.items():
                    # print("condition", k, v)
                    if self.beliefs[k] < v and t.active and self.desires[k] > v:
                        tasks.append(t)

        if tasks == []:
            tasks.append(task[0])
        
        return tasks
                
    def execute_task(self, village: Village, tasks: List[BasicNeedTask]):
        # que esto no sea random
        act_task: BasicNeedTask = random.choice(tasks)
        print(f"{self.name} is executing task {act_task.name}")
        if act_task.name == "Death":
            self._active = False
            return
        else:
            for k, v in act_task.cost.items():
                # print("cost", k, v)
                if village.get_resource(k) < v:
                    for k, v in act_task.consequences.items():
                        self.beliefs[k] += v
                    print(f"{self.name} failed to complete act_task {act_task.name}")
                    
                else:
                    village.modify_resource(k, -v)
                    for k, v in act_task.reward.items():
                        self.beliefs[k] += v
                    print(f"{self.name} completed act_task {act_task.name}")
                    
            if act_task.cost == {}:
                for k, v in act_task.reward.items():
                    self.beliefs[k] += v
                print(f"{self.name} completed act_task {act_task.name}")
                
        self.check_beliefs()
    
        
        
    