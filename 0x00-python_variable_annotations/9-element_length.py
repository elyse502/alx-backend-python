#!/usr/bin/env python3
"""
Module 9-element_length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return length of elements
    in a list
    """
    return [(i, len(i)) for i in lst]
