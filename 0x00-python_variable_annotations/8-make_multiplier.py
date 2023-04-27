#!/usr/bin/env python3
'''
functions
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    create a multiplier function
    '''
    return lambda x: x * multiplier
