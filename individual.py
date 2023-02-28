import random
import math

from constants import CHROMOSOME_LENGTH, BOUND_LOW, BOUND_UP
from utils import float_to_bin_array, bin_array_to_float


class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        x = bin_array_to_float(self)
        self.fitness_value = self.calc_fitness(x)

    @staticmethod
    def create():
        x = random.randrange(BOUND_LOW, BOUND_UP + 1)
        x_bin = float_to_bin_array(x)
        return Individual([int(x) for x in list(x_bin)])

    @staticmethod
    def clone(value):
        individual = Individual(value[:])
        individual.fitness_value = value.fitness_value
        return individual

    def mutation(self):
        probability_gene_mutation = 1.0 / CHROMOSOME_LENGTH

        for i in range(len(self)):
            if random.random() < probability_gene_mutation:
                self[i] = 0 if self[i] == 1 else 1

    def calc_fitness(self, x):
        return -1 * (0.1 * x - 1.7 * abs(math.sin(5.8 * x)) * math.cos(3.2 * x))
