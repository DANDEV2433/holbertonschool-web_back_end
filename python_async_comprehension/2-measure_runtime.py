#!/usr/bin/env python3
"""
Importing the async_comprehension function from the 1-async_comprehension
ascyncio can be used to write asynchronous code that can wait
without blocking and run several tasks at the same time.
time can be used to measure an approximate elapsed time
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Measure the total runtime of 4 parallel comprehensions
    and return the total runtime.
    Since async_generator generates 10 iterations with a 1 second
    wait each time, it takes a minimum of 10 seconds for each complete call,
    even with 4 calls because they are made in parallel with asyncio.gather.
    """
    start = time.perf_counter()
    calls = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*calls)
    end = time.perf_counter()
    return end - start
