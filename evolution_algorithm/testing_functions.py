import sys


def value_of_function(x, function):
    if function == 0:
        value = x
    elif function == 1:
        value = 0
        for i in range(len(x)):
            value += x[i] * i
    else:
        value = 0

    return value
