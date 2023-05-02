#!/usr/bin/env python3
'''
Taks 4 mandatory
'''
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    exec multiple coroutines at the same time
    """
    delay_list = []
    for _ in range(n):
        delayed = await task_wait_random(max_delay)
        delay_list.append(delayed)
        delay_list.sorted(delay_list)
    return delay_list
