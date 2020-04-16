import random as rng

from operators.replacement import *
from operators.selection import *
from options.function_types import FunctionType
from options.opt_config import get_opt_config
from options.replacement_types import ReplacementType
from options.selection_type import SelectionType
from utils.functions import *
from utils.opt_parser import *


def get_random_population():
    return []


def mutate(_population):
    raise NotImplementedError()


def crossover(_population):
    raise NotImplementedError()


def get_selection(_selection_type):
    if _selection_type == SelectionType.ROULETTE_WHEEL:
        return roulette
    elif _selection_type == SelectionType.THRESHOLD:
        return threshold
    elif _selection_type == SelectionType.TOURNAMENT:
        return tournament
    else:
        raise AttributeError("Unknown selection type", _selection_type)


def get_replacement(_replacement_type):
    if _replacement_type == ReplacementType.ELITISM:
        return elite
    elif _replacement_type == ReplacementType.GENERATION:
        return generation
    elif _replacement_type == ReplacementType.STEADY_STATE:
        return steady_state
    else:
        raise AttributeError("Unknown replacement type", _replacement_type)


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


def compute_statistics(_population):
    raise NotImplementedError()


if __name__ == "__main__":
    parser = OptParser(get_opt_config())
    parsedOptions = parser.parse(sys.argv[1:])
    print("Perform evolution algorithm with given options:\n", parsedOptions)
    function_type = FunctionType(parsedOptions["function"])
    selection_type = SelectionType(parsedOptions["sel_type"])
    replacement_type = ReplacementType(parsedOptions["rep_type"])
    crossover_probability = parsedOptions["crossover_p"] * 100
    dimensions = parsedOptions["dimensions"]
    iterations = parsedOptions["iterations"]

    fun = get_function(function_type)
    select = get_selection(selection_type)
    replace = get_replacement(replacement_type)
    population = get_random_population()

    for i in range(iterations):
        population = select(population)
        decision = rng.randrange(0, 100)
        if decision < crossover_probability:
            crossover(population)
        mutate(population)
        population = replace(population)
        compute_statistics(population)

# TODO to samo, ale z parami

# TODO eksport i porównanie wyników
