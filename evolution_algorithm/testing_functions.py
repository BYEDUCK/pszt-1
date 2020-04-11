import sys


def value_of_function(x, function):
    if function == 0:
        value = x
    elif function == 1:
        value = 0
        for i in range(len(x)):
            value += x[i] * i
    elif function == 2:
        # Pewna funkcja, która ma 2 podobne minima w różnych miejscach
        # min{x^4 0.875 + x^3 (-10.57686) + x^2 45.1 + x (-79.4) + 50}≈0.689886 at x≈1.7471
        # min{x^4 0.875 + x^3 (-10.57686) + x^2 45.1 + x (-79.4) + 50}≈0.689623 at x≈4.29684
        value = pow(x, 4) * 0.875 + pow(x, 3) * (-10.57686) + pow(x, 2) * 45.1 + x * (-79.4) + 50
    else:
        value = 0

    return value
