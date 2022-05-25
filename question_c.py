#!/usr/bin/python3

from collections import OrderedDict
from time import time, sleep

class Cache:
 
    def __init__(self, capacity: int = 3, timeout: int = 2):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.timeout = timeout
        self.timer = {}     # Record the creation time of entries
 
    def get(self, key: int) -> int:
        try:
            self.cache.move_to_end(key)
            return self.cache[key]             
        except KeyError:
            # Don't want to crash out immediately here, so only print a message
            print("Non-existent key!")
 
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.timer[key] = time()
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            # Remove the front of the dict
            self.cache.popitem(last = False)

    def update(self) -> None:
        deletion = set()
        for key in self.cache.keys():
            if self.timer[key] + self.timeout < time():
                deletion.add(key)
        for key in deletion:
            del self.cache[key]
            del self.timer[key]


if __name__ == "__main__":
    lru = Cache()
    lru.put(3, 7)
    lru.put(2, 5)
    lru.put(1, 4)
    print(lru.get(4))
    sleep(3)
    print(lru.cache)
    lru.put(999, 999)
    print(lru.cache)
    sleep(1)
    lru.update()
    print(lru.cache)

 
 

