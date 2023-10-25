#!/usr/bin/env python3
""" 2. LIFO Caching. """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache
    - Inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.key_cache = []

    def put(self, key, item):
        """ Adds an item in the cache
        """
        if key and item:
            self.key_cache.append(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('DISCARD: {}'.format(self.key_cache[-2]))
            del self.cache_data[self.key_cache.pop(-2)]

    def get(self, key):
        """ Gets an item by key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
