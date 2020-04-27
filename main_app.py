import datetime
import time

from evolution_algorithm.main_functions import *
from evolution_algorithm.stats import *
from operators.replacement import *
from operators.selection import *
from options.opt_config import get_opt_config
from options.replacement_types import ReplacementType
from options.selection_type import SelectionType
from utils.opt_parser import *

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
    cardinality = parsedOptions["cardinality"]
    attempts = parsedOptions["attempts"]
    mut_range = parsedOptions["mut_sigma"]
    x_min = parsedOptions["x_min"]
    x_max = parsedOptions["x_max"]


    fun = get_function(function_type)
    select = get_selection(selection_type)
    replace = get_replacement(replacement_type)

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
        population = get_random_population(cardinality, dimensions, x_min, x_max)

        # Loop
        pairs = make_pairs(population, fun)
        _, best_test, awg_step, pvar_step, pstdev_step = evolution_loop(iterations, pairs, crossover_probability,
                                                                        mut_range, fun, select, replace)

        test_elements = make_singles(population, fun)
        _, best_standard, awg_standard, pvar_standard, pstdev_standard = evolution_loop(iterations, test_elements,
                                                                                        crossover_probability,
                                                                                        mut_range,
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
