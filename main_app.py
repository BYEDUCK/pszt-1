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
import math
import time
import datetime

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
    pair_nr = 100
    iterations = 1000  # TODO docelowo wywalić
    dimensions = 10
    attempts = 100
    mut_range = 5  # TODO dobrac mut_range

    # Making average of @attempts results
    best_pairs = []
    best_st = []
    awg_pairs = []
    awg_st = []
    var_pairs = []
    var_st = []
    dev_pairs = []
    dev_st = []
    start = time.time()
    for h in range(attempts):
        print("\t", math.floor(h / attempts * 100), "%", end='\r')
        population = get_random_population(pair_nr * 2, dimensions)

        # Loop
        pairs = make_groups(population, 2, fun)
        _, best_test, awg_step, pvar_step, pstdev_step = testing_loop(iterations, pairs, crossover_probability,
                                                                      mut_range, fun, select, replace)

        test_elements = make_groups(population, 1, fun)
        _, best_standard, awg_standard, pvar_standard, pstdev_standard = testing_loop(iterations, test_elements,
                                                                                      crossover_probability, mut_range,
                                                                                      fun, select, replace)

        best_pairs.append(best_test)
        best_st.append(best_standard)
        awg_pairs.append(awg_step)
        awg_st.append(awg_standard)
        var_pairs.append(pvar_step)
        var_st.append(pvar_standard)
        dev_pairs.append(pstdev_step)
        dev_st.append(pstdev_standard)

    stop = time.time()
    print("\t", "100%", end='\r')

    # Compare results
    plot_statistics(best_pairs, best_st, awg_pairs, awg_st, var_pairs, var_st, dev_pairs, dev_st)

    print("Complete, calculation time: ", datetime.timedelta(seconds=(stop - start)))
