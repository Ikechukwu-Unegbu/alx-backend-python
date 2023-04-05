#!/usr/bin/env python3
import asyncio
import random

async def async_generator():
    """
    An asynchronous generator that yields a random number between 0 and 10
    after each asynchronous delay of 1 second. The generator loops 10 times.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
