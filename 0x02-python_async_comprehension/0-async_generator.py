#!/usr/bin/env python3
'''First Task file
'''
import asyncio
import random

async def async_generator():
    '''Async generator random
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
