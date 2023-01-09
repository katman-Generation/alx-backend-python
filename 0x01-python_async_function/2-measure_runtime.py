#!/usr/bin/env python3
'''Contains a method that measure the total execution time of a function'''

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the total execution time of a function"""

    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start
    return total_time / n
