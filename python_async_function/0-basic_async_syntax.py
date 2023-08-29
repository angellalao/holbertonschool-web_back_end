#!/usr/bin/env python3
"""an asynchronous coroutine 'wait_random' """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """takes an int argument, waits for a random delay between 0 and
    max delay, then returns delay time"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
