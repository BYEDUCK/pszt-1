from enum import Enum


class ReplacementType(Enum):
    GENERATION = "generation"
    GENERATION_PLUS = "generation+"
    ELITISM = "elite"
    STEADY_STATE = "steady_state"
