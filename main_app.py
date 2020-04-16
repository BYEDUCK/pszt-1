from utils.opt_parser import *
from evolution_algorithm.main_functions import *
from evolution_algorithm.testing_functions import *
from evolution_algorithm.stats import *
# import numpy
import sys
import random
import math
import copy

DEBUG = 0
BEST = 1

if __name__ == "__main__":
    parser = OptParser([OptConfig("sel_type", "s", str, "roulette"), OptConfig("rep_type", "r", str, "tournament"),
                        OptConfig("iterations", "i", int, 100)])
    parsedOptions = parser.parse(sys.argv[1:])

    print(parsedOptions)

    # TODO Check if we got needed parameters
    try:
        iterations
    except NameError:
        iterations = 20

    try:
        pair_nr
    except NameError:
        pair_nr = 10

    try:
        mut_prob
    except NameError:
        mut_prob = 0.5

    try:
        mut_range
    except NameError:
        mut_range = 1

    try:
        repr_size
    except NameError:
        repr_size = 1

    try:
        repr_dispersion
    except NameError:
        repr_dispersion = 100

    try:
        function
    except NameError:
        function = 2

    try:
        dimension
    except NameError:
        dimension = 1

    # TODO parameters compatibility check
    # if repr_size >= 1:
    #     repr_nr = pair_nr - 1
    # elif repr_size <= 0:
    #     repr_nr = 1
    # else:
    #     repr_nr = math.floor(pair_nr * repr_size)
    repr_nr = math.floor(pair_nr * repr_size)

    # TODO zrobic iles razy ten sam algorytm i wyciagnac srednia, albo jeszcze jakieś wariancje itd (może być lepiej)

    # Drawing starting points
    subject = []
    for i in range(pair_nr * 2):
        element = []
        for j in range(dimension):
            element.append(random.uniform(-100, 100))
        subject.append(element)

    # Random pairing of selected subjects
    pairs = []
    random.shuffle(subject)
    for i in range(pair_nr):
        pom0 = subject[2 * i]
        pom1 = subject[2 * i + 1]
        pairs.append([pom0, pom1, min(value_of_function(pom0, function), value_of_function(pom1, function))])

    pairs, best_test = testing_loop(iterations, pairs, mut_prob, mut_range, repr_nr, repr_dispersion, function, DEBUG,
                                    BEST)

    # TODO to samo, ale z podstawowym algorytmem

    random.shuffle(subject)
    test_elements = []
    for i in range(len(subject)):
        test_elements.append([subject[i], value_of_function(subject[i], function)])

    test_elements, best_standard = testing_loop(iterations, test_elements, mut_prob, mut_range, repr_nr,
                                                repr_dispersion, function, DEBUG, BEST)

    # Compare results
    make_statistics(pairs, test_elements, best_test, best_standard, function)
