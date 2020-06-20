from abc import ABC, abstractmethod


class FibonacciIteratorABC(ABC):
    def __init__(self, fibonacci):
        self._fibonacci = fibonacci

    @abstractmethod
    def next(self) -> int: pass

    def _get_fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self._get_fibonacci(n - 1) + self._get_fibonacci(n - 2)
