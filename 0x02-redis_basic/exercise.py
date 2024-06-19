#!/usr/bin/env python3
""" Class Cache """


import redis
from typing import Union, Any, Callable
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

    def get(self, key: str, fn: Callable) -> Any:
        """ get a key and convert it to a desired format"""
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ gets a value and convert it to a string"""
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """ gets a value and convert it to a string"""
        return self.get(key, fn=int)
