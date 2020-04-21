from options.function_types import FunctionType
from options.replacement_types import ReplacementType
from options.selection_type import SelectionType
from utils.opt_parser import OptConfig


def get_opt_config():
    return [
        OptConfig("sel_type", "s", str, "roulette", lambda s: validate_value_in_enum(s, SelectionType)),
        OptConfig("rep_type", "r", str, "generation+", lambda s: validate_value_in_enum(s, ReplacementType)),
        OptConfig("iterations", "i", int, 100, lambda x: 10 <= x <= 1000),
        OptConfig("function", "f", str, "cigar", lambda s: validate_value_in_enum(s, FunctionType)),
        OptConfig("dimensions", "d", int, 2, lambda x: 2 <= x <= 10),
        OptConfig("mutation_type", "m", str),
        OptConfig("crossover_p", "C", float, 0.5, lambda x: 0.01 <= x <= 1.0)
    ]


def validate_value_in_enum(value, enum):
    return value in map(lambda e: e.value, list(enum))
