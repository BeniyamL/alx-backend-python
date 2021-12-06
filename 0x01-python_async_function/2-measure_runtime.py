#!/usr/bin/env python3
"""
a python asynchronous module to measure the execution time
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    measure_tiem: that measures the execution time
    Arguments:
        max_delay: the maximum delay number
        n: the number of trials
    Returns:
        total time / n
    """
    initial_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    last_time = time.perf_counter()
    total_time = last_time - initial_time
    return (total_time / n)
