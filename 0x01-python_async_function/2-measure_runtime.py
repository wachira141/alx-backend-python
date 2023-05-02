#!/usr/bin/env python3
'''
measure the runtime
'''
import asyncio
import time


wait_n  = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measure exec time for wait_n(n, max_delay)
    and return total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
