#!/usr/bin/env python3
"""[Measure the runtime]
"""

import asyncio
import random
import time

from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    [Function that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function should return a float.
    Args:
        max_delay (int, optional): [maximun value of delay].
            Defaults to 10.
    Returns:
        float: [total_time / n].
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n
