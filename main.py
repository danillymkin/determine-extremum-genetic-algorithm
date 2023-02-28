from constants import POPULATION_SIZE
import numpy as np
import matplotlib.pyplot as plt

from population import Population
from utils import bin_array_to_float


def main():
    population = Population.generate(POPULATION_SIZE)

    max_fitness_values = []
    mean_fitness_values = []

    best_fitness = 0

    generation_counter = 0

    while generation_counter < 100:
        generation_counter += 1

        offspring = population.tournament()
        offspring.crossover()
        offspring.mutation()

        offspring.update_fitness_values()

        population[:] = offspring
        fitness_values = [individual.fitness_value for individual in population]

        # statistics
        max_fitness = max(fitness_values)
        mean_fitness = sum(fitness_values) / len(population)
        max_fitness_values.append(max_fitness)
        mean_fitness_values.append(mean_fitness)
        best_index = fitness_values.index(max(fitness_values))

        if max_fitness > best_fitness:
            best_fitness = max_fitness

        print(f"The population {generation_counter}: Max fitness = {max_fitness}, Mean fitness = {mean_fitness}")
        print("The best individual = ", *population[best_index])
        print("X = ", bin_array_to_float(population[best_index]), "\n")

    # charts
    show_graph_of_target_function()
    show_max_mean_fitness_graph(max_fitness_values, mean_fitness_values)


def show_graph_of_target_function():
    x = np.arange(-5, 5.0, 0.01)
    y = [0.1 * i - 1.7 * abs(np.sin(5.8 * i)) * np.cos(3.2 * i) for i in x]
    plt.plot(x, y)
    plt.axis([-10, 10, -10, 10])
    plt.grid(True)
    plt.show()


def show_max_mean_fitness_graph(max_fitness, mean_fitness):
    plt.plot(max_fitness, color='red')
    plt.plot(mean_fitness, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Mean fitness')
    plt.title('Dependence of max and mean fitness on generation')
    plt.show()


if __name__ == '__main__':
    main()
