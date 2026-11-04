#!/usr/bin/env python3
"""task of waiting for a random delay and returns the actual task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create and return an asyncio task that runs wait_random(max_delay)"""
    return asyncio.create_task(wait_random(max_delay))
