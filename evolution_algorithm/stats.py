import statistics
import matplotlib.pyplot as plt
from evolution_algorithm.testing_functions import *


def make_statistics(final_test, final_standard, best_at_step_test, best_at_step_standard, function):
    _compare_best(final_test, final_standard, function)
    _compare_every_step(best_at_step_test, best_at_step_standard, function)
    return 0


def _compare_best(test, standard, function):
    lesser_evil = 0
    for i in range(len(test[0]) - 1):
        if value_of_function(test[0][i], function) == test[0][len(test[0]) - 1]:
            lesser_evil = i
            break
    print("Solution found at tested algorithm: ", test[0][len(test[0]) - 1], " at ", test[0][lesser_evil])
    print("Solution found at standard algorithm: ", standard[0][len(standard[0]) - 1], " at ", standard[0][0])
    return 0


def _compare_every_step(test_step, standard_step, function):
    # print(test_step)
    # print(standard_step)
    plt.plot(test_step)
    plt.plot(standard_step)
    plt.xlabel("Iteration")
    plt.ylabel("Best subject")
    plt.show()
    # TODO odległość od najlepszego rozwiązania
    # TODO rozrzut elementów w danym kroku
    return 0
