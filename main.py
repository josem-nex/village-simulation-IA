import sys    
from runner import SimulationRunner
from gpt.gptAPI import clientOpenAI

PARAMETERS = {
    "iterations": 100,
    "villager_count": 10,
    "food": 100,
    "wood": 100,
    "water": 100,
    "herbs": 100,
    "stone": 50,
    "tools": 50,
    "metal": 50
}

def main():
    original_stdout = sys.stdout
    stats= None
    with open('output2.txt', 'w') as f:
        sys.stdout = f
        s = SimulationRunner(PARAMETERS)
        s.run_simulation()

        print("--------------------")
        for d in s.statistics.data:
            print(d)
        
        stats = s.statistics
        gpt = clientOpenAI()
        a = gpt.output_prompt(stats.get_statistics())
        print(a)
        sys.stdout = original_stdout


    # stats.analyze()
    stats.generate_plots()
    

if __name__ == '__main__':
    main()