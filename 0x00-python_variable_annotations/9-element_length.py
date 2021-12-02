#!/usr/bin/env python3
"""
a python function to annotate a typing
"""
from typing import Iterable, Sequence, List, Tuple


arg_type = Iterable[Sequence]
rtn_type = List[Tuple[Sequence, int]]


def element_length(lst: arg_type) -> rtn_type:
    """
    element_length- fucntion to find the length of the list
    Argument:
        lst: the given list
    Return:
        a list of tuble with sequence number & its length
    """
    return [(i, len(i)) for i in lst]
