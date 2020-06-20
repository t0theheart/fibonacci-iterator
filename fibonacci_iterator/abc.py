from abc import ABC, abstractmethod
from .iterators import FibonacciIteratorABC


class FibonacciABC(ABC):
    @abstractmethod
    def right_order_iterator(self) -> FibonacciIteratorABC: pass

    @abstractmethod
    def reverse_order_iterator(self) -> FibonacciIteratorABC: pass
