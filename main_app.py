from utils.opt_parser import *
# import numpy
# from cec17_python.cec17_functions import cec17_test_func
import sys
import random


def min_value(x, y, function):
    # TODO wyznaczac poprawnie minimum funkcji z tych dwóch argumentów
    if function == 0:
        return min(x, y)
    else:
        return -1


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
        pair_nr = 100

    try:
        mut_prob
    except NameError:
        mut_prob = 0.1

    try:
        mut_range
    except NameError:
        mut_range = 0.1

    try:
        function
    except NameError:
        function = 0

    # TODO parameters compatibility check

    # TODO test all tested functions

    subject = []
    for i in range(pair_nr * 2):
        subject.append(i)
        # TODO losowanie

    # Random pairing of selected subjects
    pairs = []
    for i in range(pair_nr):
        random.shuffle(subject)
        pom1 = subject[2 * i]
        pom2 = subject[2 * i + 1]
        pairs.append([pom1, pom2, min_value(pom1, pom2, function)])

    # print(pairs)

    # TODO start evolution (iteration loop)
    pairs.sort(key=lambda pom: pom[2])
    for i in range(iterations):
        print(i)

        # TODO reprodukcja
        # TODO krzyżowanie

        # TODO mutacja
        # Aktualnie KAŻDY z osobna może zmutować
        for j in range(len(pairs)):
            for k in range(2):
                if random.random() < mut_prob:
                    pairs[j][k] = pairs[j][k] + random.uniform(-mut_range, mut_range)
                    pairs[j][2] = min_value(pairs[j][0], pairs[j][1], function)

        # Replacing worst subjects
        pairs.sort(key=lambda pom: pom[2])
        pairs = pairs[:pair_nr]

    # TODO koniec pętli

    # TODO to samo, ale z podstawowym algorytmem

    # TODO eksport i porównanie wyników
