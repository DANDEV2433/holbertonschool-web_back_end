#!/usr/bin/env python3
"""
ascyncio can be used to write asynchronous code that can wait
without blocking and run several tasks at the same time.
time can be used to measure an approximate elapsed time
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
