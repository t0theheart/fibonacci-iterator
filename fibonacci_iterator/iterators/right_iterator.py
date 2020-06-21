from .abc import FibonacciIteratorABC


class FibonacciRightIterator(FibonacciIteratorABC):
    def next(self) -> int:
        if self._fibonacci._now >= self._fibonacci._last:
            raise StopIteration('Upper bound of the sequence.')
        n = self._fibonacci._now + 1
        _next = self._get_fibonacci(n)
        self._fibonacci._now = n
        return _next
