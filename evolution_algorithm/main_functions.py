import sys
import random
from evolution_algorithm.testing_functions import value_of_function


# TODO subject czy pair???
def mutation(marriage, probability, sigma, function):
    mutated_marriage = 0
    # TODO zrobić oba te one
    marriage[2] = min(value_of_function(marriage[0], function), value_of_function(marriage[1], function))
    return mutated_marriage


def replacing():
    return 0


def _mutate_subject(subject, probability, sigma):
    # TODO ogarnąć obsługowanie list
    if random.random() < probability:
        # TODO przerobic na Gaussa???
        subject = subject + random.uniform(-sigma, sigma)
    return subject
