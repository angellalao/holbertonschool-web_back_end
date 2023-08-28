#!/usr/bin/env python3
"""type-annotated function to_kv """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """takes a string, and int/float, returns a tuple """
    first: str = k
    second: float = v**2
    return (first, second)
