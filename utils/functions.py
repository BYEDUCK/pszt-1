import math
from functools import reduce

def griewank(x):
    part_1 = sum(map(lambda a : a**2, x))
    part_2 = reduce(lambda a, b : a * b, map(lambda a : math.cos(a[1] / math.sqrt(a[0] + 1)), enumerate(x)))
    return 1 + part_1 / 4000 - part_2


if __name__ == "__main__":
    x = [2, 2, 3]
    print(griewank(x))
