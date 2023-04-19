from constants import POPULATION_SIZE
import numpy as np
import matplotlib.pyplot as plt

from population import Population
from utils import bin_array_to_float, calc_target_function, calc_fitness

LIMIT = 100


def main():
    population = Population.generate(POPULATION_SIZE)

    max_fitness_values = []
    mean_fitness_values = []

    graph_dots = [[], [], []]

    best_fitness = 0

    generation_counter = 0

    while generation_counter < LIMIT:
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

        x = bin_array_to_float(population[best_index])

        print(f"The population {generation_counter}: Max fitness = {max_fitness}, Mean fitness = {mean_fitness}")
        print("The best individual = ", *population[best_index])
        print("X = ", x)
        print("f(x) = ", calc_target_function(x))
        print("F(x) = ", calc_fitness(x), "\n")

        if generation_counter == 1:
            for individual in population:
                ind_x = bin_array_to_float(individual)
                graph_dots[0].append([ind_x, calc_target_function(ind_x)])

        if generation_counter == 3:
            for individual in population:
                ind_x = bin_array_to_float(individual)
                graph_dots[1].append([ind_x, calc_target_function(ind_x)])

        if generation_counter == LIMIT:
            for individual in population:
                ind_x = bin_array_to_float(individual)
                graph_dots[2].append([ind_x, calc_target_function(ind_x)])

    # charts
    show_graph_of_target_function()
    show_max_mean_fitness_graph(max_fitness_values, mean_fitness_values)
    show_graph_of_fitness_function()

    for i, dots in enumerate(graph_dots):
        if i == 0:
            show_graph_of_target_function(dots, title='First generation')
        if i == 1:
            show_graph_of_target_function(dots, title='Third generation')
        if i == 2:
            show_graph_of_target_function(dots, title='Last generation')


def show_graph_of_target_function(dots=None, color='red', title='Target function'):
    plt.title(title)
    x = np.arange(-5, 5.0, 0.01)
    y = [calc_target_function(i) for i in x]

    if dots:
        for dot in dots:
            plt.scatter(dot[0], dot[1], color=color, s=20, marker='o')

    plt.plot(x, y)
    plt.axis([-10, 10, -10, 10])
    plt.grid(True)
    plt.show()


def show_graph_of_fitness_function():
    x = np.arange(-5, 5.0, 0.01)
    y = [calc_fitness(i) for i in x]
    plt.plot(x, y)
    plt.axis([-10, 10, -10, 10])
    plt.grid(True)
    plt.title('Fitness function')
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
