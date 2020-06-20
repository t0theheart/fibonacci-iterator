import unittest
from fibonacci_iterator import Fibonacci


class TestFibonacciRightIterator(unittest.TestCase):

    def test_right_iterator_case_1(self):
        f = Fibonacci()
        iterator = f.right_order_iterator()
        self.assertEqual(iterator.next(), 1)
        self.assertEqual(iterator.next(), 1)
        self.assertEqual(iterator.next(), 2)
        self.assertEqual(iterator.next(), 3)

    def test_right_iterator_case_2(self):
        f = Fibonacci(start=10)
        iterator = f.right_order_iterator()
        self.assertEqual(iterator.next(), 89)
        self.assertEqual(iterator.next(), 144)
        self.assertEqual(iterator.next(), 233)
        self.assertEqual(iterator.next(), 377)

    def test_right_iterator_case_3(self):
        f = Fibonacci(last=3)
        iterator = f.right_order_iterator()
        iterator.next()
        iterator.next()
        iterator.next()
        try:
            iterator.next()
        except StopIteration as e:
            self.assertEqual(str(e), """Can't iter to "4" elem. "3" is last.""")
