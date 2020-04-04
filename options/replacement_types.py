from enum import Enum


class ReplacementType(Enum):
    GENERATION = "generation"
    ELITISM = "elite"
    STEADY_STATE = "steady_state"
