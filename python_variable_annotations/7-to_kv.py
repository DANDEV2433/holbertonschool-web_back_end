#!/usr/bin/env python3
"""
Import Tuple and Union for type hinting
"""
from typing import Union, Tuple


"""
function to_kv that takes a string k and an int OR float v
as arguments and returns a tuple. The first element
of the tuple is the string k
The second element is the square of the int/float v
and should be annotated as a float
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a list mxd_lst of integers and floats
    and returns their sum as a float.
    """
    return str(k), float(v ** 2)
