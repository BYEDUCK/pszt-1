from options.replacement_types import ReplacementType


def generation(population):
    raise NotImplementedError("This type of replacement not implemented yet!")


def elite(population):
    raise NotImplementedError("This type of replacement not implemented yet!")


def steady_state(population):
    raise NotImplementedError("This type of replacement not implemented yet!")


def default_replacing(base, insert):
    pom_list = base + insert
    pom_list.sort(key=lambda pom: pom[len(base[0]) - 1])
    # return only best numbers
    return pom_list[:len(base)]


def get_replacement(_replacement_type):
    if _replacement_type == ReplacementType.ELITISM:
        return elite
    elif _replacement_type == ReplacementType.GENERATION:
        return generation
    elif _replacement_type == ReplacementType.STEADY_STATE:
        return steady_state
    else:
        raise AttributeError("Unknown replacement type", _replacement_type)
