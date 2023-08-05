#!/usr/bin/env python3
"""type-annotated function"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float
    """
    sum = 0
    for i in mxd_list:
        sum += i
    return sum
