#!/usr/bin/env python3
'''
Run time for parallel comprehensions
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the runtime of the async func
    using async.gather
    """
    start_t = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_t = time.perf_counter()
    return end_t - start_t
