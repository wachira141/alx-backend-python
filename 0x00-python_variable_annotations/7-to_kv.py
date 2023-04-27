#!/usr/bin/env python3
'''
string and int/float to tuple
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    take a int or float and return a tuple
    '''
    return (k, float(v**2))
