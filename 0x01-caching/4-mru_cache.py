#!/usr/bin/env python3
""" 4. MRU Caching. """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ LRUCache
    - Inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.key_cache = OrderedDict()

    def put(self, key, item):
        """ Adds an item in the cache
        """
        if not (key is None or item is None):
            if not self.key_cache:
                self.key_cache[key] = 0
            else:
                self.key_cache[key] = max(list(self.key_cache.values())) + 1

            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, discarded_value = self.key_cache.popitem()
            print('DISCARD: {}'.format(discarded_key))
            del self.cache_data[discarded_key]

    def get(self, key):
        """ Gets an item by key
        """
        if not (key is None or key not in self.cache_data.keys()):
            return self.cache_data[key]
