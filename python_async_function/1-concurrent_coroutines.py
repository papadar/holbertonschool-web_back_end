#!/usr/bin/env python3
"""Spawn multiple wait_random coroutines and collect their delays"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for finished in asyncio.as_completed(tasks):
        delays.append(await finished)

    return delays
