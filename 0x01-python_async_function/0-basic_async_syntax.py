#!/usr/bin/env python3
"""
wait random
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ 
    wait for random delay of num between 0 and 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
