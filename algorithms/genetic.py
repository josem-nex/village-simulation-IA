import random

def generate_random_individual(genes, length):
    return [random.choice(genes) for _ in range(length)]
# Generates starting chromosome population sample from a given size and genes
def generate_initial_population(size, length, genes):    
    return [generate_random_individual(genes, length) for _ in range(size)] 

# Given a list of scores it selects a pair of inidices of chromosomes to be parents 
# for the next generation using a ranked-based selection and a uniform density function
def select_parents(scores):
    rank = [i for i in range(len(scores))]
    rank.sort(key=lambda x: scores[x], reverse=True)
    rank_prob = [((2 * (len(scores)) - i) / (2 * len(scores))) for i in range(len(scores))]
    parent_indices = []

    for _ in range(2):
        random_number = random.uniform(0, 1)
        for i, p in enumerate(rank_prob):
            if random_number < p:
                parent_indices.append(rank[i])
                break
    return parent_indices

# Given two parents it generates two new children for the next generation
def crossover(parents):
    point = random.randint(1, len(parents[0]) - 1)
    child1 = parents[0][:point] + parents[1][point:]
    child2 = parents[1][:point] + parents[0][point:]
    return [child1, child2]

# Given a population, a set of genes and a ratio, it attempts to mutate a 
# random gene from an individual with a random one from the gene domain
# if it matches the ratio
def mutate(population, genes, mutation_ratio):
    for individual in population:
        if random.uniform(0, 1) < mutation_ratio:
            mutation_index = random.randint(0, len(individual) - 1)
            individual[mutation_index] = random.choice(genes)
    return population

# Given a population and their fitness scores, returns a pair of (individual, score)
# that represents the fittest individual from the population
def select_fittest(population, scores):
    sorted_scores = [i for i in range(len(scores))]
    sorted_scores.sort(key=lambda x: scores[x], reverse=True)
    best_index = sorted_scores[0]
    return [population[best_index], scores[best_index]]

def genetic_algorithm(
    pop_size, # initial population size
    length, # length of the population chromosomes
    genes, # genes to select from
    fitness, # fitness function for choromosome scoring
    mutation_ratio, # ratio for a mutation to occur in a given generation
    generations # amount of generations to generate
):
    # Initializes the population and scores for the initial inidividuals and 
    # selects the fittest
    population = generate_initial_population(pop_size, length, genes)
    scores = [fitness(individual) for individual in population]
    current_best = select_fittest(population, scores)

    for _ in range(generations):
        # Selects the parents for the new generation
        parents = [[population[i] for i in select_parents(scores)] for _ in range(pop_size // 2)]

        # As crossover returns a pair of children, the next generation pop_size remains the same as 
        # the initial parameter
        children = [crossover(parents[i]) for i in range(len(parents))]
        children = [child for sublist in children for child in sublist]

        population = mutate(children, genes, mutation_ratio)

        # Ranks new generation population
        scores = [fitness(individual) for individual in population]

        # Compares the fittest inidividual of the new generation with the existing one
        new_best = select_fittest(population, scores)
        current_best = new_best if new_best[1] > current_best[1] else current_best
    
    return current_best
