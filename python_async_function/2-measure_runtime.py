#!/usr/bin/env python3
""" 'measure_time' function """
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """takes ints n and max_delay as arguments, returns the average
    execution time for function wait_n """
    async def time():
        start = perf_counter()
        await wait_n(n, max_delay)
        end = perf_counter()
        total_time = (end - start)
        return total_time

    total_time = asyncio.run(time())
    return total_time / n
