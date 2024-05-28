#!/usr/bin/env python3
""" expiring web cache module """

import requests
from functools import wraps
from time import time
from typing import Callable

cache = {}

def cached(expire_time: int = 10):
    def decorator(func: Callable[[str], str]):
        @wraps(func)
        def wrapper(url: str):
            key = f"count:{url}"
            if key in cache and time() - cache[key][1] < expire_time:
                cache[key][0] += 1
                return cache[key][2]
            else:
                result = func(url)
                cache[key] = [1, time(), result]
                return result
        return wrapper
    return decorator

@cached()
def get_page(url: str) -> str:
    print(f"Fetching content from: {url}")
    response = requests.get(url)
    return response.text

