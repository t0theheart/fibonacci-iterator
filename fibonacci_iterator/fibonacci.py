from .abc import FibonacciABC
from .iterators import FibonacciRightIterator, FibonacciReverseIterator


class Fibonacci(FibonacciABC):
    def __init__(self, first: int = 0, last: int = 100, start=None):
        self._first = first
        self._last = last
        self._now = start or self._first

    def right_order_iterator(self) -> FibonacciRightIterator:
        return FibonacciRightIterator(self)

    def reverse_order_iterator(self) -> FibonacciReverseIterator:
        return FibonacciReverseIterator(self)
