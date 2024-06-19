#!/usr/bin/env python3
""" Class Cache """


import redis
from typing import Union
import uuid


class Cache:
    """ Class Cache """

    def __init__(self) -> None:
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
