#!/usr/bin/env python3
"""
a python function to annotatate if the input is not know
"""
from typing import Sequence, Any, Union


arg_type = Sequence[Any]
rtn_type = Union[Any, None]


def safe_first_element(lst: arg_type) -> rtn_type:
    """
    safe_first_element find the fist element of the list
    Arguments:
        lst: the given list
    Return:
        return the first element
    """
    if lst:
        return lst[0]
    else:
        return None
