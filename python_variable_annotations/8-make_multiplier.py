#!/usr/bin/env python3
"""
Import Callable for type hinting that return another function
"""
from typing import Callable


"""
function make_multiplier that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""


def make_multiplier(multiplayer: float) -> Callable[[float], float]:
    """
    function that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier.
    """
    def multiply(x: float) -> float:
        """
        function that takes a float x as argument
        and returns the product of x and multiplier.
        """
        return x * multiplayer
    return multiply
