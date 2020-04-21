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

import sys
import random

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
    iterations = 100  # TODO docelowo wywalić
    mut_range = 5  # TODO dobrac mut_range

    # TODO 25/50 iteracji
    best_pairs = []
    best_st = []
    awg_pairs = []
    awg_st = []
    var_pairs = []
    var_st = []
    dev_pairs = []
    dev_st = []
    for h in range(100):
        print(h, "%", end='\r')
        population = get_random_population(pair_nr * 2, dimensions)
        # TODO wywalić do funkcji ???
        pairs = []
        for i in range(pair_nr):
            pom0 = population[2 * i]
            pom1 = population[2 * i + 1]
            pairs.append([pom0, pom1, min(fun(pom0), fun(pom1))])

        test_elements = []
        random.shuffle(population)
        for i in range(len(population)):  # TODO ilość par czy 2* ilośc par???
            test_elements.append([population[i], fun(population[i])])

        # Loop
        pairs, best_test, awg_step, pvar_step, pstdev_step = testing_loop(iterations, pairs, crossover_probability,
                                                                          mut_range, fun, select, replace)

        test_elements, best_standard, awg_standard, pvar_standard, pstdev_standard = testing_loop(iterations,
                                                                                                  test_elements,
                                                                                                  crossover_probability,
                                                                                                  mut_range, fun,
                                                                                                  select, replace)

        best_pairs.append(best_test)
        best_st.append(best_standard)
        awg_pairs.append(awg_step)
        awg_st.append(awg_standard)
        var_pairs.append(pvar_step)
        var_st.append(pvar_standard)
        dev_pairs.append(pstdev_step)
        dev_st.append(pstdev_standard)

    print("100%", end='\r')

    # Compare results
    plot_statistics(best_pairs, best_st, awg_pairs, awg_st, var_pairs, var_st, dev_pairs, dev_st)

    print("Complete")
