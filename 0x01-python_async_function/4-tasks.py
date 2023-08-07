#!/usr/bin/env python3
"""
[Tasks]
"""

import random

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    [Function that returns the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
    Args:
        n (int, optional): [number of iterations]. Defaults to 0.
        max_delay (int, optional): [maximun value of delay].
            Defaults to 10.
    Returns:
        List[float]: [list of all the delays (float values)].
    """
    delay_list: List[float] = []
    for _ in range(n):
        delay_list.append(task_wait_random(max_delay))
    return sorted(delay_list)