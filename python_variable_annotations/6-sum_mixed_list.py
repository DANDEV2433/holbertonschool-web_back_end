#!/usr/bin/env python3
"""
Import List for type hinting a list of floats (List[float])
"""
from typing import List, Union


"""
function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a list mxd_lst of integers and floats
    and returns their sum as a float.
    """
    return sum(mxd_lst)
