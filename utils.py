from constants import BOUND_LOW, BOUND_UP, CHROMOSOME_LENGTH
import math


def float_to_bin_array(x):
    up = 2 ** CHROMOSOME_LENGTH
    x_bin = bin(round((x - BOUND_LOW) * (up - 1) / (BOUND_UP - BOUND_LOW)))[2:].zfill(20)
    return [int(x) for x in list(x_bin)]


def bin_array_to_float(bin_arr):
    up = 2 ** CHROMOSOME_LENGTH
    x_bin = ''.join([str(x) for x in bin_arr])

    return int(x_bin, 2) * (BOUND_UP - BOUND_LOW) / (up - 1) + BOUND_LOW


def calc_fitness(x):
    return -1 * calc_target_function(x) + 2.5


def calc_target_function(x):
    return 0.1 * x - 1.7 * abs(math.sin(5.8 * x)) * math.cos(3.2 * x)
