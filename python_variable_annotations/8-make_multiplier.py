#!/usr/bin/env python3
"""type-annotated function 'make_multiplier' """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float and returns a function that mutiplies it by a float """
    def function(x: float) -> float:
        return x * multiplier
    return function
