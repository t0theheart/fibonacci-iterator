from .abc import FibonacciABC
from .iterators import FibonacciRightIterator, FibonacciReverseIterator


class Fibonacci(FibonacciABC):
    def __init__(self, first: int = 0, last: int = 100):
        self._first = 0 if first < 0 else first
        self._last = last
        self._now = self._first

    def right_order_iterator(self) -> FibonacciRightIterator:
        return FibonacciRightIterator(self)

    def reverse_order_iterator(self) -> FibonacciReverseIterator:
        return FibonacciReverseIterator(self)
