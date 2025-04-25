#!/usr/bin/env python3
"""
ascyncio can be used to write asynchronous code that can wait
without blocking and run several tasks at the same time.
List can be used to store a list of values.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    function task_wait_n which takes in 2 arguments:
    n: number of times to call wait_random
    max_delay: maximum delay to wait for
    Returns a list of all the delays (float values)
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed_tasks in asyncio.as_completed(tasks):
        delay = await completed_tasks
        delays.append(delay)
    return delays
