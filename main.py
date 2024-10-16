import sys    
from runner import SimulationRunner
from gpt.gptAPI import clientOpenAI

def main():
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

    # stats.analyze()
    
    gpt = clientOpenAI()
    a = gpt.output_prompt(stats.get_statistics())
    print(a)

if __name__ == '__main__':
    main()