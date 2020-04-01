from utils.opt_parser import *
from cec17_python.cec17_functions import cec17_test_func
# niestety wywala mi błąd bo nie potrafi zaimportować biblioteki so
import sys

# TODO definicja osobnika

if __name__ == "__main__":
    parser = OptParser([OptConfig("sel_type", "s", str, "roulette"), OptConfig("rep_type", "r", str, "tournament"),
                        OptConfig("iterations", "i", int, 100)])
    parsedOptions = parser.parse(sys.argv[1:])

    print(parsedOptions)

    cec17_test_func(2, 2, 2, 2, 2)

    # TODO parameters compatibility check

    # TODO test all tested functions

    # TODO select random subject and match to pairs
    # TODO start evolution (iteration loop)

    # TODO reprodukcja
    # TODO krzyżowanie
    # TODO mutacja
    # TODO zastępowanie

    # TODO koniec pętli

    # TODO to samo, ale z podstawowym algorytmem

    # TODO eksport i porównanie wyników
