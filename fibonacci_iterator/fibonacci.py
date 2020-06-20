from .abc import FibonacciABC
from .iterators import FibonacciRightIterator, FibonacciReverseIterator


class Fibonacci(FibonacciABC):
    def __init__(self, n: int = 1):
        self._n = n

    def right_order_iterator(self) -> FibonacciRightIterator:
        return FibonacciRightIterator(self)

    def reverse_order_iterator(self) -> FibonacciReverseIterator:
        return FibonacciReverseIterator(self)
