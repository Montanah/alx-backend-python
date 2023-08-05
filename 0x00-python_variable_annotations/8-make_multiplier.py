#!/usr/bin/env python3
"""type-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier
    """
    def multiply(x: float) -> float:
        """function that multiplies the float by the multiplier"""
        return x * multiplier
    return multiply
