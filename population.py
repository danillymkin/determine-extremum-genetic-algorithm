import random

from constants import CROSSOVER_PROBABILITY, MUTATION_PROBABILITY
from individual import Individual
from utils import bin_array_to_float


class Population(list):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def generate(size=0):
        return Population([Individual.create() for i in range(size)])

    def crossover(self):
        for individual1, individual2 in zip(self[::2], self[1::2]):
            if random.random() < CROSSOVER_PROBABILITY:
                cutting_point = random.randint(2, len(individual1) - 3)
                individual1[cutting_point:], individual2[cutting_point:] = individual2[cutting_point:], individual1[cutting_point:]

    def mutation(self):
        for individual in self:
            if random.random() < MUTATION_PROBABILITY:
                individual.mutation()

    def tournament(self):
        offspring_list = []
        population_len = len(self)

        for i in range(population_len):
            individual1 = individual2 = individual3 = 0

            while individual1 == individual2 or individual1 == individual3 or individual2 == individual3:
                individual1 = random.randint(0, population_len - 1)
                individual2 = random.randint(0, population_len - 1)
                individual3 = random.randint(0, population_len - 1)

            offspring_list.append(max([self[individual1], self[individual2], self[individual3]], key=lambda individual: individual.fitness_value))

        offspring = Population(list(map(Individual.clone, offspring_list)))
        return offspring

    def update_fitness_values(self):
        for individual in self:
            x = bin_array_to_float(individual)
            individual.fitness_value = individual.calc_fitness(x)

    def get_fitness_values(self):
        return [individual.fitness_value for individual in self]
