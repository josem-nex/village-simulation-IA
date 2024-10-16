import simpy
import sys
import random

# from .agents import villager
from entities.village import Village
from VillageStatistics import VillageStatistics

class SimulationRunner:
    def __init__(self, iterations):
        self.env = simpy.Environment()
        self.iterations = iterations
        villager_count = 8
        initial_state = {
            "food": 100*villager_count,
            "wood": 100*villager_count,
            "water": 100*villager_count,
            "herbs": 100*villager_count,
            "stone": 50,
            "tools": 50,
            "metal": 50
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
            self.village.care_villagers()
            best = self.village.select_actions()
            actions = self.village.actions

            for i, _ in enumerate(self.village.villagers):
                rand = random.randint(0, 1)
                if rand >= 0.75:
                    for action in actions:
                        new = best
                        new[i] = action

                        new_value = self.village.actions_fitness(new)
                        best_value = self.village.actions_fitness(best)

                        if new_value > best_value:
                            best = new
                            print(f"Villager {i} has selected a new action: {action.name}")
                            break

            self.village.state.show_state()

            self.statistics.record(self.env.now, self.village.state.get_state(), self.village.state.villager_count)
            
            print("Actions to execute: ")
            print([x.name for x in best])
            self.village.execute_actions(best)
            
            self.village.check_villagers_status()
            self.village.care_villagers()
            self.village.apply_daily_cost()
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
    
    

