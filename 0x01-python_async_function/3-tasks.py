#!/usr/bin/env python3
"""
a python asynchronous module to return a task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    task_wait_random: call wait random & returns the task
    Arguments:
        max_delay: the maximum delay number
    Returns:
        the task
    """
    t = asyncio.create_task(wait_random(max_delay))
    return (t)
