from .abc import FibonacciIteratorABC


class FibonacciReverseIterator(FibonacciIteratorABC):
    def next(self) -> int:
        n = self._fibonacci._n - 1
        _next = self._get_fibonacci(n)
        self._fibonacci._n = n
        return _next
