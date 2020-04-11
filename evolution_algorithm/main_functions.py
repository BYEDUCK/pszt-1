import sys
import random
from evolution_algorithm.testing_functions import value_of_function


# TODO dorobić aby działało też dla zwykłego ewolucyjnego
# Mutation of ONLY one number
def mutate(pair, sigma):
    x = random.randint(0, 1)
    if (type(pair[0]) == int or type(pair[0]) == float) and (type(pair[1]) == int or type(pair[1]) == float):
        pair[x] = random.gauss(pair[x], sigma)
    elif type(pair[0]) == list and type(pair[1]) == list:
        y = random.randint(0, len(pair) - 1)
        pair[x][y] = random.gauss(pair[x][y], sigma)
    # TODO Czy sopdziewamy się czegoś innego niż int/float lub list???
    else:
        sys.exit('Mutation - unknown pair element')
    return pair


def crossover(base, pair):
    pom = random.randint(0, len(base) - 1)
    pom_pair = base[pom]
    if (type(pair[0]) == int or type(pair[0]) == float) and (type(pair[1]) == int or type(pair[1]) == float):
        pair[0] = random.uniform(pair[0], pom_pair[0])
        pair[1] = random.uniform(pair[1], pom_pair[1])
    elif type(pair[0]) == list and type(pair[1]) == list:
        pom_list_x = []
        pom_list_y = []
        for i in range(len(pair[0])):
            pom_list_x.append(random.uniform(pair[0][i], pom_pair[0][i]))
            pom_list_y.append(random.uniform(pair[1][i], pom_pair[1][i]))
        pair[0] = pom_list_x
        pair[1] = pom_list_y
    # TODO Czy sopdziewamy się czegoś innego niż int/float lub list???
    else:
        sys.exit('Crossover - unknown pair element')
    return pair


def replacing(base, insert):
    pom_list = base + insert
    pom_list.sort(key=lambda pom: pom[2])
    # return only best numbers
    return pom_list[:len(base)]
