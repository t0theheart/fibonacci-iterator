import unittest
from fibonacci_iterator import Fibonacci


class TestFibonacciReverseIterator(unittest.TestCase):

    def test_reverse_iterator_case_1(self):
        f = Fibonacci(start=5)
        iterator = f.reverse_order_iterator()
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 2)
        self.assertEqual(iterator.next(), 1)
        self.assertEqual(iterator.next(), 1)

    def test_reverse_iterator_case_2(self):
        f = Fibonacci(start=10)
        iterator = f.reverse_order_iterator()
        self.assertEqual(iterator.next(), 34)
        self.assertEqual(iterator.next(), 21)
        self.assertEqual(iterator.next(), 13)
        self.assertEqual(iterator.next(), 8)

    def test_reverse_iterator_case_3(self):
        f = Fibonacci(first=3, start=6)
        iterator = f.reverse_order_iterator()
        iterator.next()
        iterator.next()
        iterator.next()
        try:
            iterator.next()
        except StopIteration as e:
            self.assertEqual(str(e), """Can't iter to "2" elem. "3" is first.""")