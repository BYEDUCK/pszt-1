from utils.opt_parser import *
import sys

if __name__ == "__main__":
    parser = OptParser([OptConfig("sel_type", "s", str, "roulette"), OptConfig("rep_type", "r", str, "tournament"), OptConfig("iterations", "i", int, 100)])
    parsedOptions = parser.parse(sys.argv[1:])
    print(parsedOptions)
