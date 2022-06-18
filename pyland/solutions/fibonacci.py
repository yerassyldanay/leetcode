from collections import defaultdict as dd

class Solution:
    def __init__(self):
        self.d = dd()

    def fibonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        if n not in self.d:
            self.d[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)

        return self.d[n]

from functools import lru_cache

@lru_cache(None)
def fib(i):
    if i == 0 or i == 1:
        return i

    return fib(i - 1) + fib(i - 2)

def fib2(i):
    if i == 0 or i == 1:
        return i

    return fib2(i - 1) + fib2(i - 2)

import time

start = time.time()
fib2(50)
print(time.time() - start)

start = time.time()
fib(50)
print(time.time() - start)

# 0 1 1 2 3 5 8 13 21 34 55
