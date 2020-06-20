from .abc import FibonacciIteratorABC


class FibonacciReverseIterator(FibonacciIteratorABC):
    def next(self) -> int:
        if self._fibonacci._now <= self._fibonacci._first:
            raise StopIteration(f'"{self._fibonacci._now}" is the first elem')
        n = self._fibonacci._now - 1
        _next = self._get_fibonacci(n)
        self._fibonacci._now = n
        return _next
