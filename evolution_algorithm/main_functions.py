import sys
import random
from evolution_algorithm.testing_functions import value_of_function


# Mutation of ONLY one number
def mutate(pair, sigma):
    x = random.randint(0, 1)
    # TODO float
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


# UNUSED
def mutation(base, probability, sigma, function):
    mutated = []
    for i in range(len(base)):
        marriage = base[i]
        mutated_marriage = []
        if type(marriage[0]) == int and type(marriage[1]) == int:
            # mutated_marriage[0] = _mutate_subject(marriage[0], probability, sigma)
            # mutated_marriage[1] = _mutate_subject(marriage[1], probability, sigma)
            return 0
        elif type(marriage[0]) == list and type(marriage[1]) == list:
            # mutated_marriage[0] = _mutate_list(marriage[0], probability, sigma)
            # mutated_marriage[1] = _mutate_list(marriage[1], probability, sigma)
            return 0
        # TO DO Czy sopdziewamy się czegoś innego niż int lub list???
        else:
            return 0

        mutated_marriage[2] = min(value_of_function(mutated_marriage[0], function),
                                  value_of_function(mutated_marriage[1], function))
        mutated.append(mutated_marriage)
        # TO DO sprawdzić czy to działa poprawnie
    return mutated


def replacing(base, insert):
    pom_list = base + insert
    pom_list.sort(key=lambda pom: pom[2])
    # return only best numbers
    return pom_list[:len(base)]
