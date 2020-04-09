from utils.opt_parser import *
from evolution_algorithm.main_functions import *
# import numpy
# from cec17_python.cec17_functions import cec17_test_func
import sys
import random
import math
import statistics
import copy

DEBUG = 1
BEST = 1


def min_value(x, y, function):
    # TODO wyznaczac poprawnie minimum funkcji z tych dwóch argumentów
    if function == 0:
        return min(math.sin(x), math.sin(y))
    else:
        return -1


def cross_values(x, y, function):
    if type(x[0]) == int and type(y[0]) == int:
        pom0 = statistics.mean([x[0], y[0]])
        pom1 = statistics.mean([x[1], y[1]])
        out = [pom0, pom1, min_value(pom0, pom1, function)]
    # TODO sprawdzić czy to działa jak powinno
    elif type(x[0]) == list and type(y[0]) == list:
        pom_list_x = []
        pom_list_y = []
        for i in range(len(x[0])):
            pom_list_x.append(statistics.mean([x[i][0], y[i][0]]))
            pom_list_y.append(statistics.mean([x[i][1], y[i][1]]))
        out = [pom_list_x, pom_list_y, min_value(pom_list_x, pom_list_y, function)]
    else:
        out = [0, 0, 0]

    return out


if __name__ == "__main__":
    parser = OptParser([OptConfig("sel_type", "s", str, "roulette"), OptConfig("rep_type", "r", str, "tournament"),
                        OptConfig("iterations", "i", int, 100)])
    parsedOptions = parser.parse(sys.argv[1:])

    print(parsedOptions)

    # Check if we got needed parameters
    try:
        iterations
    except NameError:
        iterations = 50

    try:
        pair_nr
    except NameError:
        pair_nr = 10

    try:
        mut_prob
    except NameError:
        mut_prob = 0.2

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
        function = 0

    # TODO parameters compatibility check
    if repr_size >= 1:
        repr_nr = pair_nr - 1
    elif repr_size <= 0:
        repr_nr = 1
    else:
        repr_nr = math.floor(pair_nr * repr_size)

    # TODO test all tested functions

    subject = []
    for i in range(pair_nr * 2):
        subject.append(i * 10)
        # TODO losowanie

    # Random pairing of selected subjects
    pairs = []
    random.shuffle(subject)
    for i in range(pair_nr):
        pom0 = subject[2 * i]
        pom1 = subject[2 * i + 1]
        pairs.append([pom0, pom1, min_value(pom0, pom1, function)])

    # TODO zrobic iles razy ten sam algorytm i wyciagnac srednia

    # TODO start evolution (iteration loop)
    pairs.sort(key=lambda pom: pom[2])
    if DEBUG:
        print("default", pairs)

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

        # # Crossing
        # crossing(pom_pair, "TO DO")
        # if DEBUG:
        #     print("crossed", pom_pair, "\t", len(pom_pair))
        #
        # # Mutation
        # pom_pair = mutation(pom_pair, mut_prob, mut_range, function)
        # if DEBUG:
        #     print("mutated", pom_pair, "\t", len(pom_pair))

        new_pairs = []
        # Cross or mutate (all have to do sth)
        for j in range(len(pom_pair)):
            if random.random() < mut_prob:
                pom = mutate(pom_pair[j], mut_range)
            else:
                pom = crossover(pom_pair, pom_pair[j])
            new_pairs.append([pom, min(value_of_function(pom[0], function), value_of_function(pom[1], function))])

        # Replacing worst subjects
        if DEBUG:
            print("not substituted", pairs, "\t", len(pairs))
        pairs = replacing(pairs, pom_pair)
        if DEBUG:
            print("substituted", pairs, "\t", len(pairs))

        if BEST:
            print("best", pairs[0][2])

    if BEST:
        print([row[2] for row in pairs])

    # TODO koniec pętli

    # TODO to samo, ale z podstawowym algorytmem

    # TODO eksport i porównanie wyników
