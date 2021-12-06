#!/usr/bin/env python3
"""
a python asynchronous module that waits a random delay b/n 0 & max-delay up
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    await_n: that wait a random number b/n 0 to max-delya of n tries
    Arguments:
        max_delay: the maximum delay number
        n: the number of trials
    Returns:
        list of the random numbers in order
    """
    t: List = []
    d: List[float] = []
    for i in range(n):
        t.append(task_wait_random(max_delay))

    for tsk in asyncio.as_completed(t):
        dly = await tsk
        d.append(dly)

    return (d)
