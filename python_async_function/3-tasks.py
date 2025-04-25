#!/usr/bin/env python3
"""
ascyncio can be used to write asynchronous code that can wait
without blocking and run several tasks at the same time.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function that takes in an integer max_delay and returns a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
