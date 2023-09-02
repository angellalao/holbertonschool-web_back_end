#!/usr/bin/env python3
""" coroutine called 'measure_runtime' """
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes async_comprehension 4 times in parallel, returns the
    total runtime"""
    start = perf_counter()
    coroutines = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coroutines)
    end = perf_counter()
    total_time = (end - start)
    return total_time
