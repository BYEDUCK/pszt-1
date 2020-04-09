import sys
import random
from evolution_algorithm.testing_functions import value_of_function


# Mutation of ONLY one number
def mutate(pair, sigma):
    x = random.randint(0, 1)
    if type(pair[0]) == int and type(pair[1]) == int:
        pair[x] = random.gauss(pair[x], sigma)
    elif type(pair[0]) == list and type(pair[1]) == list:
        y = random.randint(0, len(pair) - 1)
        pair[x][y] = random.gauss(pair[x][y], sigma)
    # TODO Czy sopdziewamy się czegoś innego niż int lub list???
    else:
        return 0
    return pair


def crossover(base, pair):
    return 0


# UNUSED
def mutation(base, probability, sigma, function):
    mutated = []
    for i in range(len(base)):
        marriage = base[i]
        mutated_marriage = []
        if type(marriage[0]) == int and type(marriage[1]) == int:
            mutated_marriage[0] = _mutate_subject(marriage[0], probability, sigma)
            mutated_marriage[1] = _mutate_subject(marriage[1], probability, sigma)
        elif type(marriage[0]) == list and type(marriage[1]) == list:
            mutated_marriage[0] = _mutate_list(marriage[0], probability, sigma)
            mutated_marriage[1] = _mutate_list(marriage[1], probability, sigma)
        # TODO Czy sopdziewamy się czegoś innego niż int lub list???
        else:
            return 0

        mutated_marriage[2] = min(value_of_function(mutated_marriage[0], function),
                                  value_of_function(mutated_marriage[1], function))
        mutated.append(mutated_marriage)
        # TODO sprawdzić czy to działa poprawnie
    return mutated


def replacing(base, insert):
    pom_list = base + insert
    pom_list.sort(key=lambda pom: pom[2])
    # return only best numbers
    return pom_list[:len(base)]


# UNUSED
def crossing(base, costam):
    crossed = []
    random.shuffle(base)
    i = 0
    while i < len(pom_pair) - 1:
        if random.random() < cross_prob:
            pom = cross_values(pom_pair[i], pom_pair[i + 1], function)
            del pom_pair[i:i + 2]
            pom_pair.insert(i, pom)
        i += 1

    return 0


# UNUSED
def _mutate_subject(subject, probability, sigma):
    # TODO ogarnąć obsługiwanie list
    if random.random() < probability:
        # TODO przerobic na Gaussa???
        subject = subject + random.uniform(-sigma, sigma)
    return subject


# UNUSED
def _mutate_list(list, probability, sigma):
    # TODO
    return list
