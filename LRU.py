# doc
from collections import deque

class LRU:
    _cache = {}
    _q = None
    _size = 0

    def __init__(self, size=None):
        if size is None:
            size = 10
        self._size = size
        self._q = deque([])
        self._cache = {}

    def add(self, key, value):
        if key in self._cache:
            self._update(key, value)
        else:
            self._add_new(key, value)

    def _add_new(self, key, value):
        if len(self._cache) == self._size:
            self.remove()
        self._cache[key] = value
        self._q.append({'key': key, 'value': value})

    def _update(self, key, value):
        self._q.remove({'value': self._cache[key], 'key': key})
        self._cache[key] = value
        self._q.append({'value': value, 'key': key})

    def _remove(self):
        del self._cache[self._q.popleft()['key']]

    def stringify(self):
        print(self._cache)

    def get_cache(self):
        return self._cache

    def get_queue(self):
        return self._q
