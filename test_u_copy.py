import unittest
from deque_class_copy import Deque


class Test_cases(unittest.TestCase):

    def test_pop_push_tail(self):
        deque = Deque()
        self.assertEqual(deque.pop_tail(), None)
        deque.push_tail(9)
        self.assertEqual(deque.pop_tail(), 9)

    def test_size(self):
        deque = Deque()
        deque.push_tail(34)
        deque.push_tail(1)
        deque.push_tail(2)
        deque.push_head(0)
        deque.push_head(10)
        self.assertEqual(deque.size(), 5)

    def test_pop_push_head(self):
        deque = Deque()
        self.assertEqual(deque.pop_head(), None)
        deque.push_head(34)
        self.assertEqual(deque.pop_head(), 34)

    def test_clear(self):
        deque = Deque()
        deque.push_head(34)
        deque.push_head(1)
        deque.push_tail(2)
        deque.clear()
        self.assertEqual(deque.size(), 0)

    def test_empty(self):
        deque = Deque()
        self.assertEqual(deque.pop_head(), None)
        self.assertEqual(deque.pop_tail(), None)
        self.assertEqual(deque.size(), 0)

    def test_diff_pop(self):
        deque = Deque()
        deque.push_tail(10)
        deque.push_tail(11)
        deque.push_tail(12)
        self.assertEqual(deque.pop_tail(), 12)
        self.assertEqual(deque.pop_head(), 10)

    def test_diff_push(self):
        deque = Deque()
        deque.push_head(1)
        deque.push_head(2)
        deque.push_tail(3)
        deque.push_tail(4)
        self.assertEqual(deque.pop_head(), 2)
        self.assertEqual(deque.pop_tail(), 4)

if __name__ == "__name__":
    unittest.main()
