from utils.opt_parser import *
from evolution_algorithm.main_functions import *
# import numpy
# from cec17_python.cec17_functions import cec17_test_func
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

    # Check if we got needed parameters
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
        cross_prob
    except NameError:
        cross_prob = 0.5

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

    # TODO parameters compatibility check
    # if repr_size >= 1:
    #     repr_nr = pair_nr - 1
    # elif repr_size <= 0:
    #     repr_nr = 1
    # else:
    #     repr_nr = math.floor(pair_nr * repr_size)
    repr_nr = math.floor(pair_nr * repr_size)

    # TODO test all tested functions

    subject = []
    for i in range(pair_nr * 2):
        element = []
        for j in range(4):
            element.append(j * i * 4.72)
        # subject.append(element)
        subject.append(i * 3.14)
        # TODO losowanie

    # Random pairing of selected subjects
    pairs = []
    random.shuffle(subject)
    for i in range(pair_nr):
        pom0 = subject[2 * i]
        pom1 = subject[2 * i + 1]
        pairs.append([pom0, pom1, min(value_of_function(pom0, function), value_of_function(pom1, function))])

    # TODO zrobic iles razy ten sam algorytm i wyciagnac srednia, albo jeszcze jakieś wariancje itd (może być lepiej)

    pairs.sort(key=lambda pom: pom[2])
    if DEBUG:
        print("default", pairs)

    # Iteration loop of evolution algorithm
    for i in range(iterations):
        if DEBUG:
            print("iteration", i)

        pom_pair = []
        if DEBUG:
            print("start", pom_pair)
        # TODO reprodukcja
        for j in range(repr_nr):
            pom = math.floor(abs(random.gauss(0, repr_dispersion)))
            while pom >= pair_nr:
                pom = math.floor(abs(random.gauss(0, repr_dispersion)))
            pom_pair.append(copy.deepcopy(pairs[pom]))
        if DEBUG:
            print("reproducted", pom_pair, "\t", len(pom_pair))

        new_pairs = []
        # Cross or mutate (all have to do sth)
        for j in range(len(pom_pair)):
            pom = []
            if random.random() < mut_prob:
                pom = mutate(pom_pair[j], mut_range)
            else:
                pom = crossover(pom_pair, pom_pair[j])
            pom[2] = min(value_of_function(pom[0], function), value_of_function(pom[1], function))
            new_pairs.append(pom)

        # Replacing worst subjects
        if DEBUG:
            print("Cross or mutation", new_pairs, "\t", len(new_pairs))
            print("not substituted", pairs, "\t", len(pairs))
        pairs = replacing(pairs, new_pairs)
        if DEBUG:
            print("substituted", pairs, "\t", len(pairs))

        if BEST:
            print("best", pairs[0])

    if BEST:
        print([row[2] for row in pairs])

    # TODO to samo, ale z podstawowym algorytmem

    # TODO eksport i porównanie wyników
