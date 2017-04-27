import unittest
from collections import deque
import LRU


class Test(unittest.TestCase):


    def test_add(self):
        lru = LRU.LRU(100)
        lru.add(1, 'item1')
        self.assertEqual(lru.get_cache(), {1: 'item1'})
        self.assertEqual(lru.get_queue(), deque([{'value': 'item1', 'key': 1}]))

    def test_update(self):
        lru = LRU.LRU(100)
        lru.add(1, 'item1')
        lru.add(1, 'item2')
        self.assertEqual(lru.get_cache(), {1: 'item2'})
        self.assertEqual(lru.get_queue(), deque([{'value': 'item2', 'key': 1}]))

    def test_full_add(self):
        lru = LRU.LRU(3)
        lru.add(1, 'item1')
        lru.add(2, 'item2')
        lru.add(3, 'item3')
        self.assertEqual(lru.get_cache(), {1: 'item1', 2: 'item2', 3: 'item3'})
        self.assertEqual(lru.get_queue(), deque([{'value': 'item1', 'key': 1},
                                                {'value': 'item2', 'key': 2},
                                                {'value': 'item3', 'key': 3}]))
        lru.add(4, 'item4')
        self.assertEqual(lru.get_cache(), {2: 'item2', 3: 'item3', 4: 'item4'})
        self.assertEqual(lru.get_queue(), deque([{'value': 'item2', 'key': 2},
                                                {'value': 'item3', 'key': 3},
                                                {'value': 'item4', 'key': 4}]))

    def test_full_update(self):
        lru = LRU.LRU(3)
        lru.add(1, 'item1')
        lru.add(2, 'item2')
        lru.add(3, 'item3')
        self.assertEqual(lru._cache, {1: 'item1', 2: 'item2', 3: 'item3'})
        self.assertEqual(lru._q, deque([{'value': 'item1', 'key': 1},
                                        {'value': 'item2', 'key': 2},
                                        {'value': 'item3', 'key': 3}]))
        lru.add(1, 'new_item1')
        self.assertEqual(lru._cache, {2: 'item2', 3: 'item3', 1: 'new_item1'})
        self.assertEqual(lru._q, deque([{'value': 'item2', 'key': 2},
                                        {'value': 'item3', 'key': 3},
                                        {'value': 'new_item1', 'key': 1}]))


if __name__ == '__main__':
    unittest.main()
