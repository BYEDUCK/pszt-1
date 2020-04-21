import matplotlib.pyplot as plt


def plot_statistics(best_pairs, best_standard, awg_pairs, awg_standard, var_pairs, var_standard, dev_pairs,
                    dev_standard):
    _compare_every_step(_average_results(best_pairs), _average_results(best_standard),
                        "Najlepsza wartość funkcji w kolejnych iteracjach")
    _compare_every_step(_average_results(awg_pairs), _average_results(awg_standard),
                        "Średnia wartość funkcji w kolejnych iteracjach")
    _compare_every_step(_average_results(var_pairs), _average_results(var_standard),
                        "Wariancja wartości funkcji w kolejnych iteracjach")
    # _compare_every_step(_average_results(dev_pairs), _average_results(dev_standard),
    #                     "Odchylenie standardowe wartości funkcji w kolejnych iteracjach")
    return 0


def _average_results(in_data):
    pom = [0 for x in range(len(in_data[0]))]
    for i in range(len(in_data)):
        for j in range(len(in_data[0])):
            pom[j] += in_data[i][j]

    averaged = []
    for i in range(len(pom)):
        averaged.append(pom[i] / len(in_data[0]))

    return averaged


def _compare_every_step(tested, standard, title):
    plt.plot(tested)
    plt.plot(standard)
    if tested[len(tested) - 1] >= 0 and standard[len(standard) - 1] > 0:
        plt.yscale("log")
    plt.grid(True, which="both")
    plt.title(title)
    plt.xlabel("Iteracja")
    plt.ylabel("Wartość")
    plt.legend(["Testowany", "Standardowy"])
    plt.show()

    return 0
