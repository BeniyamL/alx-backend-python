#!/usr/bin/env python3
"""
a python function to annotates list of string & floats & int

"""
from typing import Union, Tuple


input_type = Union[float, int]
output_type = Tuple[str, float]


def to_kv(k: str, v: input_type) -> output_type:
    """
    to_kv function to return a tuple combination of str & float
    Arguments:
        k: the given string
        v: the given float or int number
    Return:
        the a tuple combination of str & sqrt of the number
    """
    output: output_type = (k, v**2)
    return (output)
