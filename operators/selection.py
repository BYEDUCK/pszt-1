from options.selection_type import SelectionType

import random

# TODO ma bugi (jak dostaje identczne wyniki po całości to suma prob = 0)
def roulette(population, size):
    # prob = []
    # for i in range(len(population)):
    #     if i > 0:
    #         prob.append(
    #             abs(population[i][len(population[i]) - 1] - population[len(population) - 1][len(population[i]) - 1]) +
    #             prob[i - 1])
    #     else:
    #         prob.append(
    #             abs(population[i][len(population[i]) - 1] - population[len(population) - 1][len(population[i]) - 1]))
    #
    # selected = []
    # for i in range(size):
    #     pom = random.uniform(0, prob[len(prob) - 1])
    #     for j in range(len(prob)):
    #         if pom < prob[j]:
    #             selected.append(population[j])
    #             break
    # return selected
    return population


def tournament(population):
    raise NotImplementedError("This type of selection not implemented yet!")


def threshold(population):
    raise NotImplementedError("This type of selection not implemented yet!")


def get_selection(_selection_type):
    if _selection_type == SelectionType.ROULETTE_WHEEL:
        return roulette
    elif _selection_type == SelectionType.THRESHOLD:
        return threshold
    elif _selection_type == SelectionType.TOURNAMENT:
        return tournament
    else:
        raise AttributeError("Unknown selection type", _selection_type)
