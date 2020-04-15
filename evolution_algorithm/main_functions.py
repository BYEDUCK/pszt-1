from evolution_algorithm.testing_functions import *
import sys
import random
import math
import copy


# Mutation of ONLY one number
def mutate(subject, sigma):
    x = random.randint(0, len(subject) - 2)
    if type(subject[0]) == int or type(subject[0]) == float:
        subject[x] = random.gauss(subject[x], sigma)
    elif type(subject[0]) == list:
        y = random.randint(0, len(subject[x]) - 1)
        subject[x][y] = random.gauss(subject[x][y], sigma)
    # TODO Czy sopdziewamy się czegoś innego niż int/float lub list???
    else:
        sys.exit('Mutation - unknown subject element')
    return subject


def crossover(base, subject):
    pom = random.randint(0, len(base) - 1)
    pom_pair = base[pom]
    if type(subject[0]) == int or type(subject[0]) == float:
        for i in range(len(subject) - 1):
            subject[i] = random.uniform(subject[i], pom_pair[i])
    elif type(subject[0]) == list:
        pom_lists = [[0 for x in range(len(subject[0]))] for y in range(len(subject))]
        for i in range(len(subject) - 1):
            for j in range(len(subject[i])):
                pom_lists[i][j] = (random.uniform(subject[i][j], pom_pair[i][j]))
        subject = pom_lists
    # TODO Czy sopdziewamy się czegoś innego niż int/float lub list???
    else:
        sys.exit('Crossover - unknown subject element')
    return subject


def replacing(base, insert):
    pom_list = base + insert
    pom_list.sort(key=lambda pom: pom[len(base[0]) - 1])
    # return only best numbers
    return pom_list[:len(base)]


def testing_loop(iterations, population, mut_prob, mut_range, repr_nr, repr_dispersion, function, DEBUG, BEST):
    population.sort(key=lambda pom: pom[len(pom) - 1])
    if DEBUG:
        print("default", population)

    best_test = []
    for i in range(iterations):
        if DEBUG:
            print("iteration", i)

        pom_pair = []
        if DEBUG:
            print("start", pom_pair)
        # TODO reprodukcja
        for j in range(repr_nr):
            pom = math.floor(abs(random.gauss(0, repr_dispersion)))
            while pom >= len(population):
                pom = math.floor(abs(random.gauss(0, repr_dispersion)))
            pom_pair.append(copy.deepcopy(population[pom]))
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
            pom[len(pom) - 1] = min(value_of_function(pom[0], function), value_of_function(pom[1], function))
            new_pairs.append(pom)

        # Replacing worst subjects
        if DEBUG:
            print("Cross or mutation", new_pairs, "\t", len(new_pairs))
            print("not substituted", population, "\t", len(population))
        population = replacing(population, new_pairs)
        if DEBUG:
            print("substituted", population, "\t", len(population))

        if BEST:
            print("best", population[0])
        best_test.append(population[0][len(population[0]) - 1])

    if BEST:
        print([row[len(row) - 1] for row in population])

    return population, best_test
