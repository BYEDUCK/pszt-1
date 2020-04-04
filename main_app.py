from options.opt_config import get_opt_config
from utils.opt_parser import *

# TODO definicja osobnika

if __name__ == "__main__":
    parser = OptParser(get_opt_config())
    parsedOptions = parser.parse(sys.argv[1:])

    print(parsedOptions)

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
