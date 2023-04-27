#!/usr/bin/env python3
'''
complex types - mixed list
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    take a mixed list of int and floats
    return sum as float
    '''
    return float(sum(mxd_lst))
