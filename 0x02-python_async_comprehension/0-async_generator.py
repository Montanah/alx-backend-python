#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random

from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main() -> None:
    """ Main Function """
    async for i in async_generator():
        print(i) # should wait for 1 second before printing another random number