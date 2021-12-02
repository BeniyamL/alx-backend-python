#!/usr/bin/env python3
"""
a python function to annotates list of floats
"""
from typing import List


list_type = List[float]


def sum_list(input_list: list_type) -> float:
    """ sum_list function to find the sum of a float list
    Arguments:
        input_list: the given list with float number
    Return:
        the sum of the list
    """
    sum: float = 0
    for n in input_list:
        sum += n
    return (sum)
