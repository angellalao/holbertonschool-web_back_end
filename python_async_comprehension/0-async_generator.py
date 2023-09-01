#!/usr/bin/env python3
""" coroutine called 'async generator' """
import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """loop 10 times, each time asynchronously wait 1 second, then
    yield a random number between 0 and 10 """
    for count in range(10):
        num = random.uniform(0, 10)
        yield num
        await asyncio.sleep(1)
