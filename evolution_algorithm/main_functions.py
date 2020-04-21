from utils.functions import *

import sys
import random
import copy
import statistics as stat

DEBUG = 0
BEST = 1


def get_random_population(length, dimension):
    subject = []
    for i in range(length):
        element = []
        for j in range(dimension):
            element.append(random.uniform(-100, 100))
        subject.append(element)
    return subject


def mutation(_population, mut_range, func):
    for i in range(len(_population)):
        _population[i] = mutate(_population[i], mut_range)
        _population[i][len(_population[i]) - 1] = min_of_function(_population[i], func)
    return 0


def mutate(subject, sigma):
    x = random.randint(0, len(subject) - 2)
    if type(subject[0]) == int or type(subject[0]) == float:
        sys.exit('Mutation - int or float')
    elif type(subject[0]) == list:
        y = random.randint(0, len(subject[x]) - 1)
        subject[x][y] = random.gauss(subject[x][y], sigma)
    else:
        sys.exit('Mutation - unknown subject element')
    return subject


def crossing(pairs, children, crossover_probability, func):
    for i in range(len(children)):
        if random.random() < crossover_probability:
            children[i] = crossover(pairs, children[i])
            children[i][len(children[i]) - 1] = min_of_function(children[i], func)
    return 0


def crossover(base, subject):
    pom = random.randint(0, len(base) - 1)
    pom_pair = base[pom]
    if type(subject[0]) == int or type(subject[0]) == float:
        sys.exit('Crossover - int or float')
    elif type(subject[0]) == list:
        # TODO przyjrzeć się bo mam wątpliwości
        pom_lists = [[0 for x in range(len(subject[0]))] for y in range(len(subject))]
        for i in range(len(subject) - 1):
            for j in range(len(subject[i])):
                pom_lists[i][j] = (random.uniform(subject[i][j], pom_pair[i][j]))
        subject = pom_lists
    else:
        sys.exit('Crossover - unknown subject element')
    return subject


def testing_loop(iterations, population, cross_prob, mut_range, fun, select, replace):
    population.sort(key=lambda pom: pom[len(pom) - 1])
    DEBUG = 0
    if DEBUG:
        print("default", population)

    best_step = []
    awg_step = []
    pvar_step = []
    pstdev_step = []
    for i in range(iterations):
        if i > 15 and best_step[i-1] == best_step[i - 11]:
            DEBUG = 1

        if DEBUG:
            print("iteration", i)

        # Reproduction
        if DEBUG:
            print("start", population)
        children = copy.deepcopy(select(population, math.floor(len(population) * 1.5)))
        if DEBUG:
            print("reproducted", children, "\t", len(children))

        # Cross
        crossing(population, children, cross_prob, fun)

        # Mutate
        mutation(children, mut_range, fun)

        # Replacing worst subjects
        if DEBUG:
            print("Cross or mutation", children, "\t", len(children))
            print("not substituted", population, "\t", len(population))
        population = replace(population, children)
        if DEBUG:
            print("substituted", population, "\t", len(population))

        stat_pom = []
        for j in range(len(population)):
            stat_pom.append(population[j][len(population[0]) - 1])

        awg_step.append(stat.mean(stat_pom))
        pvar_step.append(stat.pvariance(stat_pom))
        pstdev_step.append(stat.pstdev(stat_pom))
        best_step.append(population[0][len(population[0]) - 1])

        if BEST:
            print("best", best_step[i])
        if DEBUG:
            print("awg", awg_step[i], "\t", "variance", pvar_step[i], "\t", "st deviation", pstdev_step[i], "\t", )

    if BEST:
        print([row[len(row) - 1] for row in population])

    return population, best_step, awg_step, pvar_step, pstdev_step
