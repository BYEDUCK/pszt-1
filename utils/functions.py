import math
from functools import reduce

from options.function_types import FunctionType


# http://infinity77.net/global_optimization/test_functions_nd_A.html


# min 0
def griewank(x):
    part_1 = _sum_of_squares(x)
    part_2 = reduce(lambda a, b: a * b, map(lambda a: math.cos(a[1] / math.sqrt(a[0] + 1)), enumerate(x)))
    return 1 + part_1 / 4000 - part_2


# min 0
def schwefel(x):
    return 418.9829 * len(x) - sum(map(lambda a: a * math.sin(math.sqrt(abs(a))), x))


# min 0
def alpine_1(x):
    return sum(map(lambda a: abs(a * math.sin(a) + 0.1 * a), x))


# min 0
def cigar(x, c=1000000):
    return x[0] ** 2 + c * _sum_of_squares(x[1:])


# min 0
def ackley(x):
    n = len(x)
    part_1 = math.exp(-0.2 * math.sqrt(1 / n * _sum_of_squares(x)))
    part_2 = math.exp(1 / n * sum(map(lambda a: math.cos(2 * math.pi * a), x)))
    return -20 * part_1 - part_2 + 20 + math.e


# min -106.7645367198034
def bird(x):
    # two dimensional only!
    if len(x) != 2:
        raise ValueError("this function can only be 2d")
    part_1 = math.sin(x[0]) * math.exp((1 - math.cos(x[1])) ** 2)
    part_2 = math.cos(x[1]) * math.exp((1 - math.sin(x[0])) ** 2)
    part_3 = (x[0] - x[1]) ** 2
    return part_1 + part_2 + part_3


# min 0.39788735772973816
def branin_1(x):
    # two dimensional only!
    if len(x) != 2:
        raise ValueError("this function can only be 2d")
    part_1 = -1.275 * ((x[0] ** 2) / (math.pi ** 2)) + (5 * (x[0] / math.pi)) + x[1] - 6
    part_2 = (10 - (5 / (4 * math.pi))) * math.cos(x[0])
    return part_1 ** 2 + part_2 + 10


def _sum_of_squares(x):
    return sum(map(lambda a: a ** 2, x))


def get_function(_function_type):
    if _function_type == FunctionType.ALPINE_1:
        return alpine_1
    elif _function_type == FunctionType.CIGAR:
        return cigar
    elif _function_type == FunctionType.GRIEWANK:
        return griewank
    elif _function_type == FunctionType.SCHWEFEL:
        return schwefel
    elif _function_type == FunctionType.ACKLEY:
        return ackley
    elif _function_type == FunctionType.BIRD:
        return bird
    elif _function_type == FunctionType.BRANIN_1:
        return branin_1
    else:
        raise AttributeError("Unknown function type", _function_type)


def min_of_function(subject, fun):
    min_temp = fun(subject[0])
    for j in range(len(subject) - 1):
        min_temp = min(min_temp, fun(subject[j]))
    return min_temp


if __name__ == "__main__":
    x = [2, 2, 3]
    x1 = [0, 5]
    print(griewank(x))
    print(schwefel(x))
    print(alpine_1(x))
    print(cigar(x1))
