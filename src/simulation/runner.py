import simpy
import sys

# from .agents import villager
from entities.village import Village
from VillageStatistics import VillageStatistics

class SimulationRunner:
    def __init__(self, iterations):
        self.env = simpy.Environment()
        self.iterations = iterations
        initial_state = {
            "food": 50,
            "wood": 40,
            "water": 20,
            "herbs": 5,
            "stone": 10,
            "tools": 3,
            "metal": 0
        }
        self.village = Village(initial_state, villagers=5)
        # self.villager.state.show_state()
        self.statistics = VillageStatistics()

    def run_simulation(self):
        print('Simulation started')
        self.env.process(self.village_process('Village 1', 0, 5))
        print(f"start villager count: {len(self.village.villagers)}")
        self.env.run(until=self.iterations)
        print(f"end village count: {len(self.village.villagers)}")
        self.village.state.show_state()

    def village_process(self, name, arrival_time, service_time):
        while True:
            if (len(self.village.villagers) == 0):
                print('Village has no villagers left')
                print(f"Day {self.env.now}")
                return
            print(f"Day {self.env.now}")
            # print("villagers prepares for new day")
            actions = self.village.select_actions()
            self.village.state.show_state()
            
            self.statistics.record(self.env.now, self.village.state.get_state(), self.village.state.villager_count)
            
            self.village.execute_actions(actions)
            
            self.village.apply_daily_cost()
            self.village.check_villagers_status()
            self.village.care_villagers()
            # print('village is selecting a task sequence...')
            # self.village.state.show_state()
            # print("villagers recover from last day")
            # self.village.care_villagers()
            yield self.env.timeout(1)



original_stdout = sys.stdout

stats= None

with open('output.txt', 'w') as f:
    sys.stdout = f
    s = SimulationRunner(100)
    s.run_simulation()
    
    print("--------------------")
    for d in s.statistics.data:
        print(d)
    sys.stdout = original_stdout
    
    stats = s.statistics

stats.analyze()
    
    

