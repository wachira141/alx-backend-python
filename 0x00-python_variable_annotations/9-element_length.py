#!/usr/bin/env python3
'''
Task 9 module
'''
from from typing import Iterable, List, Sequence, Tuple


def element_length(lst: iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Computes the length of a list of sequence.
    '''
    return [(i, len(i)) for i in lst]
