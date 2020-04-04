from utils.opt_parser import *
# import numpy
# from cec17_python.cec17_functions import cec17_test_func
import sys
import random
import math
import statistics
import copy
DEBUG = 0
BEST = 1


def min_value(x, y, function):
    # TODO wyznaczac poprawnie minimum funkcji z tych dwóch argumentów
    if function == 0:
        return min(x, y)
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

    # x: Solution vector
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # nx: Number of dimensions
    nx = 10
    # mx: Number of objective functions
    mx = 1
    # func_num: Function number
    func_num = 1
    # Pointer for the calculated fitness
    f = [0]

    # cec17_test_func(x, f, nx, mx, func_num)

    # Check if we got needed parameters
    try:
        iterations
    except NameError:
        iterations = 100

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
        subject.append(i)
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

        # TODO krzyżowanie
        random.shuffle(pom_pair)
        i = 0
        while i < len(pom_pair) - 1:
            if random.random() < cross_prob:
                pom = cross_values(pom_pair[i], pom_pair[i + 1], function)
                del pom_pair[i:i + 2]
                pom_pair.insert(i, pom)
            i += 1
        if DEBUG:
            print("crossed", pom_pair, "\t", len(pom_pair))

        # TODO mutacja
        for j in range(len(pom_pair)):
            for k in range(2):
                if random.random() < mut_prob:
                    # print(j, "\t", k, "\t", len(pom_pair), "\t", len(pom_pair[j]), "\t", pom_pair[j], "\t",
                    #       pom_pair[j][k])
                    pom_pair[j][k] = pom_pair[j][k] + random.uniform(-mut_range, mut_range)
                    pom_pair[j][2] = min_value(pom_pair[j][0], pom_pair[j][1], function)
        if DEBUG:
            print("mutated", pom_pair, "\t", len(pom_pair))

        # TODO wybierać najlepsze sztuki, czy zastępować te złe?
        # Replacing worst subjects
        if DEBUG:
            print("not substituted", pairs, "\t", len(pairs))
        pairs = pairs[:pair_nr - len(pom_pair)] + pom_pair
        if DEBUG:
            print("substituted", pairs, "\t", len(pairs))

        pairs.sort(key=lambda pom: pom[2])
        if DEBUG:
            print("sorted", pairs, "\t", len(pairs))
        if BEST:
            print("best", pairs[0][2])

    if BEST:
        print([row[2] for row in pairs])

    # TODO koniec pętli

    # TODO to samo, ale z podstawowym algorytmem

    # TODO eksport i porównanie wyników
