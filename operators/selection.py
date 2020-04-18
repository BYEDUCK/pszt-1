from options.selection_type import SelectionType


def roulette(population):
    return population
    # raise NotImplementedError("This type of selection not implemented yet!")


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
