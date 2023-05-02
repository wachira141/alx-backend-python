#!/usr/bin/env python3
'''
Taks 3
'''
import asyncio



def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    return an async.Task
    """
    task = async.create_task(wait_random(max_delay))
    return task
