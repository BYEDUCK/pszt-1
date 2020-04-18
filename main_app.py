from operators.replacement import *
from operators.selection import *
from options.function_types import FunctionType
from options.opt_config import get_opt_config
from options.replacement_types import ReplacementType
from options.selection_type import SelectionType
from utils.functions import *
from utils.opt_parser import *

from evolution_algorithm.main_functions import *
from evolution_algorithm.stats import *
# import numpy
import sys
import random


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
    # TODO zaimplementować
    return 0


if __name__ == "__main__":
    parser = OptParser(get_opt_config())
    parsedOptions = parser.parse(sys.argv[1:])
    print("Perform evolution algorithm with given options:\n", parsedOptions)
    function_type = FunctionType(parsedOptions["function"])
    selection_type = SelectionType(parsedOptions["sel_type"])
    replacement_type = ReplacementType(parsedOptions["rep_type"])
    crossover_probability = parsedOptions["crossover_p"]
    dimensions = parsedOptions["dimensions"]
    iterations = parsedOptions["iterations"]

    fun = get_function(function_type)
    select = get_selection(selection_type)
    replace = get_replacement(replacement_type)

    # Meke population and pair population with same same start points
    pair_nr = 10
    iterations = 10
    mut_range = 5  # TODO dobrac mut_range
    population = get_random_population(pair_nr * 2, dimensions)
    # TODO wywalić do funkcji
    pairs = []
    for i in range(pair_nr):
        pom0 = population[2 * i]
        pom1 = population[2 * i + 1]
        # pairs.append([pom0, pom1, min(value_of_function(pom0, fun), value_of_function(pom1, fun))])
        pairs.append([pom0, pom1, min(fun(pom0), fun(pom1))])

    test_elements = []
    for i in range(len(population)):
        # test_elements.append([population[i], value_of_function(population[i], fun)])
        test_elements.append([population[i], fun(population[i])])

    # Loop
    pairs, best_test = testing_loop(iterations, pairs, crossover_probability, mut_range, fun, select, replace)

    test_elements, best_standard = testing_loop(iterations, test_elements, crossover_probability, mut_range, fun,
                                                select, replace)

    # TODO zrobic iles razy ten sam algorytm i wyciagnac srednia, albo jeszcze jakieś wariancje itd (może być lepiej)

    # Compare results
    # make_statistics(pairs, test_elements, best_test, best_standard, function)
