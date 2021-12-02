#!/usr/bin/env python3
"""
a python function to annotates a callable function
"""
from typing import Callable


out_type = Callable[[float], float]


def make_multiplier(multiplier: float) -> out_type:
    """
    make_multiplier - a function to multiply a number by the function
    Arguments:
        multiplier: the multiplier number
    Return:
        the function that multiply a number by multiplier
    """
    def mul(n: float) -> float:
        return float(n * multiplier)

    return mul
