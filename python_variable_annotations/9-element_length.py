#!/usr/bin/env python3
"""
Iterable what can be covered with a loop
List type that represents a list of objects
Tuple type that represents a tuple of objects
Sequence is a type with an order and a length
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function which takes as parameter lst, an iterable which contains
    sequences, the function returns a list of tuples with for each tuple
    (sequence and int its length)
    """
    return [(i, len(i)) for i in lst]
