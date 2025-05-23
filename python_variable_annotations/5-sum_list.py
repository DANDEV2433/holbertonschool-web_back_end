#!/usr/bin/env python3
"""
Import List for type hinting a list of floats (List[float])
"""
from typing import List


"""
function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """
    a list input_list of floats as argument
    and returns their sum as a float
    """
    return sum(input_list)
