#!/usr/bin/env python3
'''
execute multiple coroutines
at the same time
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    receive 2 int and return 
    a list ordered in ascending order
    """
    delay_list = []
    for _ in range(n):
        conc_tasks =await wait_random(max_delay)
        delay_list.append(conc_tasks)
    return sorted(delay_list)
