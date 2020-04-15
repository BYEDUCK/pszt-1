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
    print(test_step)
    print(standard_step)

    plt.plot(test_step)
    plt.plot(standard_step)
    plt.title("Najlepsze dopasowanie funkcji w każdej iteracji")
    plt.xlabel("Iteration")
    plt.ylabel("Best subject")
    plt.legend(["Tested", "Standard"])
    plt.inferno()
    plt.show()

    # TODO odległość od najlepszego rozwiązania
    test_delta = []
    for i in range(len(test_step)):
        test_delta.append(abs(test_step[i] - test_step[len(test_step) - 1]))
    standard_delta = []
    for i in range(len(standard_step)):
        standard_delta.append(abs(standard_step[i] - standard_step[len(standard_step) - 1]))

    plt.plot(test_delta)
    plt.plot(standard_delta)
    plt.title("Odległość od najlepszego znalezionego rozwiązania")
    plt.xlabel("Iteration")
    plt.ylabel("Distance")
    plt.legend(["Tested", "Standard"])
    plt.autumn()
    plt.show()

    # TODO rozrzut elementów w danym kroku
    test_mean = []
    test_median = []
    test_variance = []
    test_pstdev = []
    for i in range(len(test_step)):
        test_delta.append(abs(test_step[i] - test_step[len(test_step) - 1]))
    standard_mean = []
    standard_median = []
    standard_variance = []
    standard_pstdev = []
    for i in range(len(standard_step)):
        standard_delta.append(abs(standard_step[i] - standard_step[len(standard_step) - 1]))

    return 0
