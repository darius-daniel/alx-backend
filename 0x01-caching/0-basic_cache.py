#!/usr/bin/env python3
""" 0. Basic Dictionary. """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache
    - Inherits from BaseCaching
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if not (key is None or key not in self.cache_data.keys()):
            return self.cache_data[key]
