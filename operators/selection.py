import random

from options.selection_type import SelectionType


def roulette(population, size):
    prob = []
    for i in range(len(population)):
        if i > 0:
            prob.append(abs(population[i][-1] - population[-1][-1]) + prob[i - 1])
        else:
            prob.append(abs(population[i][-1] - population[-1][-1]))

    selected = []
    if prob[-1] > 0:
        for i in range(size):
            pom = random.uniform(0, prob[len(prob) - 1])
            for j in range(len(prob)):
                if pom < prob[j]:
                    selected.append(population[j])
                    break
    else:
        for i in range(size):
            selected.append(population[random.randint(0, len(population) - 1)])
    return selected


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
