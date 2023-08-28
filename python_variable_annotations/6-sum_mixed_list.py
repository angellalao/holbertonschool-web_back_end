#!/usr/bin/env python3
"""type-annotated function sum_mixed_list """
from typing import List, Optional, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """takes a list of ints and floats and returns the sum as a float"""
    result = 0
    for num in mxd_list:
        result = result + num
    return result
