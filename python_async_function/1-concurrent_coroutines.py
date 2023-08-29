#!/usr/bin/env python3
"""asyncronous coroutine 'wait_n' """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes 2 int arguments(number of delays , max delay time) and return the
    list of delays in asc order """
    return_list = []
    for num in range(n):
        delay = await wait_random(max_delay)
        return_list.append(delay)
    sorted_return_list = sorted(return_list)
    return sorted_return_list
