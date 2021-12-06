#!/usr/bin/env python3
"""
a python asynchronous module that waits a random delay b/n 0 & max-delay 
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    await_function: that wait a random number b/n 0 to max-delay
    Arguments:
        max_delay: the maximum delay number
    Returns:
        the random number that waits
    """
    d: float = random.uniform(0, max_delay)
    await asyncio.sleep(d)
    return (d)
