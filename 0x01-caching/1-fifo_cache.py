#!/usr/bin/env python3
""" 1. FIFO Caching. """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache
    - Inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Adds an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[0]
            print('DISCARD: {}'.format(discarded_key))
            del self.cache_data[discarded_key]

    def get(self, key):
        """ Gets an item by key
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
