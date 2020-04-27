import copy
import random
import statistics as stat
import sys

from utils.functions import *

DEBUG = 0
BEST = 0


def make_pairs(population, func):
    return make_groups(population, 2, func)


def make_singles(population, func):
    return make_groups(population, 1, func)


def make_groups(population, size_of_group, func):
    if len(population) % size_of_group != 0:
        sys.exit('Can\'t group elements')

    group = []
    random.shuffle(population)
    for i in range(math.floor(len(population) / size_of_group)):
        pom = []
        for j in range(size_of_group):
            pom.append(population[size_of_group * i + j])
        pom.append(0)
        pom[size_of_group] = min_of_function(pom, func)
        group.append(pom)

    return group



def get_random_population(length, dimension, x_min, x_max):

    subject = []
    for i in range(length):
        element = []
        for j in range(dimension):
            element.append(random.uniform(x_min, x_max))
        subject.append(element)
    return subject


def mutation(_population, mut_range, func):
    for i in range(len(_population)):
        _population[i] = mutate(_population[i], mut_range)
        _population[i][-1] = min_of_function(_population[i], func)
    return 0


def mutate(subject, sigma):
    # Mutate one in union
    # x = random.randint(0, len(subject) - 2)

    # Mutate one in every person in union
    for x in range(len(subject) - 1):
        y = random.randint(0, len(subject[x]) - 1)
        subject[x][y] = random.gauss(subject[x][y], sigma)
    return subject


def crossing(pairs, children, crossover_probability, func):
    for i in range(len(children)):
        if random.random() < crossover_probability:
            children[i] = crossover(pairs, children[i])
            # Wywalone w celu optymalizacji - dopóki mutation jest obowiązkowe to poniższe jest niepotrzebne
            # children[i][len(children[i]) - 1] = min_of_function(children[i], func)
    return 0


def crossover(base, subject):
    # TODO przyjrzeć się bo mam wątpliwości
    pom = random.randint(0, len(base) - 1)
    pom_pair = base[pom]
    pom_lists = [[0 for x in range(len(subject[0]))] for y in range(len(subject))]
    for i in range(len(subject) - 1):
        for j in range(len(subject[i])):
            pom_lists[i][j] = (random.uniform(subject[i][j], pom_pair[i][j]))
    subject = pom_lists
    return subject


def evolution_loop(iterations, population, cross_prob, mut_range, fun, select, replace):
    population.sort(key=lambda pom: pom[-1])
    if DEBUG:
        print("default", population)

    best_step = []
    awg_step = []
    pvar_step = []
    pstdev_step = []
    for i in range(iterations):
        if DEBUG or BEST:
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
            stat_pom.append(population[j][-1])

        awg_step.append(stat.mean(stat_pom))
        pvar_step.append(stat.pvariance(stat_pom))
        pstdev_step.append(stat.pstdev(stat_pom))
        best_step.append(population[0][-1])

        if BEST:
            print([row[-1] for row in population])
            print("best", population[0])
        if DEBUG:
            print("awg", awg_step[i], "\t", "variance", pvar_step[i], "\t", "st deviation", pstdev_step[i], "\t", )

    if BEST:
        print([row[-1] for row in population])

    return population, best_step, awg_step, pvar_step, pstdev_step
