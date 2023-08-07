#!/usr/bin/env python3
"""[Concurrent Coroutines]
"""

import asyncio
import random

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """[Asynchronous coroutine that takes in an integer argument
        (max_delay, with a default value of 10) named wait_random
        that waits for a random delay between 0 and max_delay
        (included and float value) seconds and eventually returns it.
    Args:
        max_delay (int, optional): [maximun value of delay].
            Defaults to 10.
    Returns:
        float: [random delay between 0 and max_delay].
    """
    delay_list: List[float] = []
    for _ in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)