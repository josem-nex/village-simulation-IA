import simpy

# from .agents import villager
from src.simulation.entities.village import Village

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
        self.village = Village(initial_state, villagers=6)
        # self.villager.state.show_state()

    def run_simulation(self):
        print('Simulation started')
        self.env.process(self.village_process('Village 1', 0, 5))
        self.env.run(until=self.iterations)

    def village_process(self, name, arrival_time, service_time):
        while True:
            print("villagers prepares for new day")
            self.village.care_villagers()
            print('village is selecting a task sequence...')
            self.village.select_actions()
            # print("villagers recover from last day")
            # self.village.care_villagers()
            yield self.env.timeout(1)

s = SimulationRunner(5)
s.run_simulation()
