from src.simulation.runner import SimulationRunner

if __name__ == '__main__':
    runner = SimulationRunner(30*12*5)
    runner.run_simulation()