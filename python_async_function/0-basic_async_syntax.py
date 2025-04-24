#!/usr/bin/env python3
"""
ascyncio can be used to write asynchronous code that can wait
without blocking and run several tasks at the same time.
random can be used to generate random values.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    function which expects a random delay between 0 and max_delay
    and returns this delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
