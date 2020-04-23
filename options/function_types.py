from enum import Enum


class FunctionType(Enum):
    GRIEWANK = "griewank"
    SCHWEFEL = "schwefel"
    ALPINE_1 = "alpine-1"
    CIGAR = "cigar"
    ACKLEY = "ackley"
    BIRD = "bird"
    BRANIN_1 = "branin-1"
