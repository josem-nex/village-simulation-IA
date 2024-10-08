from BDI.Entities.Village import Village
from BDI.Entities.Villager import Villager



def main():
    
    aldea = Village("Aldea", [], resources={"food": 100, "water": 100, "wood": 100})
    
    juan = Villager("Juan", "M", 20, health=0.5, fullness=0.2, hydration=0.8, energy=0.3)
    
    for i in range(10):
        juan.execute_task(aldea, juan.generate_tasks())
        
    print(juan.beliefs)
    print(aldea.resources)

if __name__ == "__main__":
    main()