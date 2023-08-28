#!/usr/bin/env python3
"""type-annotated function 'sum_list' """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats and returns the sum as a float """
    answer = 0
    for num in input_list:
        answer = answer + num
    return answer
