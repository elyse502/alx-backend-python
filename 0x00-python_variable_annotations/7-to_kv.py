#!/usr/bin/env python3
"""
Module 7-to_kv
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a int or float
    and returns a tuple of the string
    and a float
    """
    return (k, v**2)
