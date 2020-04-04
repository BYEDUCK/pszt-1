from utils.opt_parser import OptConfig


def get_opt_config():
    return [
        OptConfig("sel_type", "s", str, "roulette"),
        OptConfig("rep_type", "r", str, "tournament"),
        OptConfig("iterations", "i", int, 100, lambda x: 10 <= x <= 1000),
        OptConfig("function", "f", str, "cigar"),
        OptConfig("dimensions", "d", int, 2, lambda x: 2 <= x <= 10),
        OptConfig("mutation_p", "M", float, 0.1, lambda x: 0.01 <= x <= 1.0),
        OptConfig("mutation_type", "m", str),
        OptConfig("crossover_p", "C", float, 0.5, lambda x: 0.01 <= x <= 1.0),
        OptConfig("crossover_type", "c", str)
    ]
