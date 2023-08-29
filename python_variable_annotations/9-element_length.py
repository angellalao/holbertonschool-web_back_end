#!/usr/bin/env python3
"""annotated function 'element length' """
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """takes an iterable of sequences and returns a list of tuples
    containing each sequence and its length"""
    return [(i, len(i)) for i in lst]
