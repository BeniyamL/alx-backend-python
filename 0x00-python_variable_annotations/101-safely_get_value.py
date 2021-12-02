#!/usr/bin/env python3
"""
a python function to annotatate if the input is not know
"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')
arg_type = Union[T, None]
rtn = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: arg_type= None) -> rtn:
    """
    safely_get_value function to safely get a value
    Arguments:
        dct: the given dictionary
        key: the key of the dict
        default: the default value
    Return:
        a given value or None if it is not found
    """
    if key in dct:
        return dct[key]
    else:
        return default
