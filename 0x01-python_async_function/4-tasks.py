#!/usr/bin/env python3
"""
[Tasks]
"""

import asyncio
import random

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    [Function that returns a list of delays in ascending order].
    Args:
        max_delay (int): [maximun value of delay].
    Returns:
        List[float]: [list of delays in ascending order].
    """
    delay_list: List[float] = []
    for _ in range(n):
        delay_list.append(task_wait_random(max_delay))
    return sorted(delay_list)
