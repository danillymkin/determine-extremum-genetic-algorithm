import random
import math

from constants import CHROMOSOME_LENGTH, BOUND_LOW, BOUND_UP
from utils import float_to_bin_array, bin_array_to_float, calc_fitness


class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        x = bin_array_to_float(self)
        self.fitness_value = calc_fitness(x)

    @staticmethod
    def create():
        x = random.uniform(BOUND_LOW, BOUND_UP)
        x_bin = float_to_bin_array(x)
        return Individual([int(x) for x in list(x_bin)])

    @staticmethod
    def clone(value):
        individual = Individual(value[:])
        individual.fitness_value = value.fitness_value
        return individual

    def mutation(self):
        gene_for_mutation = random.randint(0, CHROMOSOME_LENGTH - 1)
        self[gene_for_mutation] = 0 if self[gene_for_mutation] == 1 else 1
