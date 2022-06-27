#!/user/bin/env python3
"""
create asynchrounous coroutine that generate random
"""

import asyncio
import random

async def wait_random(max_delay = 10):
    """ wait random func that have max_delay paramater """
    rand = random.uniform(0, max_delay)
    return rand 
