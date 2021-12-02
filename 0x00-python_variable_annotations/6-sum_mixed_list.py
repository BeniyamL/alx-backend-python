#!/usr/bin/env python3
"""
a python function to annotates list of floats & int
"""
from typing import List, Union


list_type = List[Union[float, int]]


def sum_mixed_list(mxd_lst: list_type) -> float:
    """
    sum_mixed_list function to find the sum of a float * int list
    Arguments:
        mxd_list: the given mixed list
    Return:
        the sum of the list
    """
    sum: float = 0
    for n in mxd_lst:
        sum += n
    return (sum)
