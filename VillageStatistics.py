import matplotlib
# matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

class VillageStatistics:
    def __init__(self):
        self.data = []

    def record(self, iteration, village_state, villager_count):
        self.data.append({
            'iteration': iteration,
            'state': village_state.copy(),
            'villager_count': villager_count
        })

    def get_statistics(self):
        return self.data

    def parse_state(self, state):
        """Extract resource name and its value from the state string"""
        resources = {}
        for resource in state:
            resource_name, values = resource.split(":")
            status, amount = values.strip()[1:-1].split(", ")
            resources[resource_name.strip()] = float(amount)
        return resources

    def generate_plots(self):
        """Generates plots for each resource and villager count over time"""
        iterations = [entry['iteration'] for entry in self.data]
        villager_count = [entry['villager_count'] for entry in self.data]
        
        # Extract resources
        resources = ['food', 'wood', 'water', 'herbs', 'stone', 'tools', 'metal']
        resource_data = {resource: [] for resource in resources}

        for entry in self.data:
            parsed_state = self.parse_state(entry['state'])
            for resource in resources:
                resource_data[resource].append(parsed_state[resource])

        # Plot each resource
        for resource in resources:
            plt.figure(figsize=(10, 5))
            plt.plot(iterations, resource_data[resource], label=resource, marker='o')
            plt.xlabel('Iteration')
            plt.ylabel(f'{resource.capitalize()} Amount')
            plt.title(f'{resource.capitalize()} Over Time')
            plt.legend()
            plt.grid(True)
            # plt.show()
            plt.savefig(f'plots/{resource}_plot.png')  # Guarda el gráfico
            plt.close()  # Cierra la figura para liberar memoria

        # Plot villager count
        plt.figure(figsize=(10, 5))
        plt.plot(iterations, villager_count, label='Villager Count', marker='o', color='purple')
        plt.xlabel('Iteration')
        plt.ylabel('Villager Count')
        plt.title('Villager Count Over Time')
        plt.legend()
        plt.grid(True)
        # plt.show()
        plt.savefig('plots/villager_count_plot.png')  # Guarda el gráfico
        plt.close()  # Cierra la figura

    def analyze(self):
        """Analyzes the trends in the village simulation"""
        # Example analysis: finding trends of depletion or growth
        resources = ['food', 'wood', 'water', 'herbs', 'stone', 'tools', 'metal']
        resource_data = {resource: [] for resource in resources}

        for entry in self.data:
            parsed_state = self.parse_state(entry['state'])
            for resource in resources:
                resource_data[resource].append(parsed_state[resource])

        # Analyze trends for each resource
        conclusions = {}
        for resource in resources:
            values = np.array(resource_data[resource])
            change_rate = np.diff(values)
            avg_change = np.mean(change_rate)
            status = "increasing" if avg_change > 0 else "decreasing" if avg_change < 0 else "stable"
            conclusions[resource] = {
                'avg_change': avg_change,
                'trend': status
            }

        # Print analysis conclusions
        for resource, analysis in conclusions.items():
            print(f"{resource.capitalize()}:")
            print(f"  Average Change: {analysis['avg_change']:.2f}")
            print(f"  Trend: {analysis['trend']}\n")
