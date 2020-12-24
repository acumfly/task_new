import unittest
from deque_class import Deque


class Test_cases(unittest.TestCase):

    def test_pop_push_tail(self):
        deque = Deque()
        deque.push_tail("Hello")
        deque.push_tail(1)
        deque.push_tail(2)
        deque.push_head(0)
        deque.push_head(10)
        self.assertEqual(deque.pop_tail(), 2)

    def test_size(self):
        deque = Deque()
        deque.push_tail(34)
        deque.push_tail(1)
        deque.push_tail(2)
        deque.push_head(0)
        deque.push_head(10)
        deque.size()
        self.assertEqual(deque.size(), 5)

    def test_pop_push_head(self):
        deque = Deque()
        deque.push_head(34)
        deque.push_head(1)
        deque.push_tail(2)
        self.assertEqual(deque.pop_head(), 1)

    def test_clear(self):
        deque = Deque()
        deque.push_head(34)
        deque.push_head(1)
        deque.push_tail(2)
        deque.clear()
        self.assertEqual(deque.size(), 0)

if __name__ == "__name__":
    unittest.main()
