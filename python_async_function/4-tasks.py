#!/usr/bin/env python3
"""asyncronous coroutine 'task_wait_n' """
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """takes 2 int arguments(number of delays , max delay time) and return the
    list of delays in asc order """
    return_list = []
    for num in range(n):
        delay = await task_wait_random(max_delay)
        return_list.append(delay)
    sorted_return_list = sorted(return_list)
    return sorted_return_list
