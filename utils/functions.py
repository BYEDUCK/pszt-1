import math
from functools import reduce

from options.function_types import FunctionType


def griewank(x):
    part_1 = _sum_of_squares(x)
    part_2 = reduce(lambda a, b: a * b, map(lambda a: math.cos(a[1] / math.sqrt(a[0] + 1)), enumerate(x)))
    return 1 + part_1 / 4000 - part_2


def schwefel(x):
    return 418.9829 * len(x) - sum(map(lambda a: a * math.sin(math.sqrt(abs(a))), x))


def alpine_1(x):
    return sum(map(lambda a: abs(a * math.sin(a) + 0.1 * a), x))


def cigar(x, c=1000000):
    return x[0] ** 2 + c * _sum_of_squares(x[1:])


def cosine_mixture(x):
    part_1 = sum(map(lambda a: math.cos(5 * math.pi * a), x))
    part_2 = _sum_of_squares(x)
    return -0.1 * part_1 - part_2


def _sum_of_squares(x):
    return sum(map(lambda a: a ** 2, x))


def get_function(_function_type):
    if _function_type == FunctionType.ALPINE_1:
        return alpine_1
    elif _function_type == FunctionType.CIGAR:
        return cigar
    elif _function_type == FunctionType.COSINE_MIXTURE:
        return cosine_mixture
    elif _function_type == FunctionType.GRIEWANK:
        return griewank
    elif _function_type == FunctionType.SCHWEFEL:
        return schwefel
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
