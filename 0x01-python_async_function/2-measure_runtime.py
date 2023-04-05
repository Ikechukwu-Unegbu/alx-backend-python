#!/usr/bin/env python3
'''Task zero.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    
    '''Calculate average runtime of wait_n.
    '''
    begin_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - begin_time) / n
