#!/usr/bin/env python3
"""
[Tasks]
"""

import asyncio
import random

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    [Function that returns a asyncio.Task].
    Args:
        max_delay (int): [maximun value of delay].
    Returns:
        asyncio.Task: [asyncio.Task].
    """
    return asyncio.create_task(wait_random(max_delay))
