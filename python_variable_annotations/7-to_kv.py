#!/usr/bin/env python3
"""
Import List for type hinting a list of floats (List[float])
"""
from typing import Union, Tuple


"""
function to_kv that takes a string k and an int OR float v
as arguments and returns a tuple. The first element
of the tuple is the string k
The second element is the square of the int/float v
and should be annotated as a float
"""


def to_kv(K: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a list mxd_lst of integers and floats
    and returns their sum as a float.
    """
    return str(K), float(v) ** 2
