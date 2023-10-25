#!/usr/bin/env python3
""" 4. MRU Caching. """
from base_caching import BaseCaching
from collections import OrderedDict


def get_mru(cache):
    """ Returns the most recently used key
    """
    most_recent = sorted(cache.values(), reverse=True)[1]
    for k, v in cache.items():
        if v == most_recent:
            return k


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
        if key and item:
            if not self.key_cache:
                self.key_cache[key] = 0
            else:
                self.key_cache[key] = max(list(self.key_cache.values())) + 1

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = get_mru(self.key_cache)
                print('DISCARD: {}'.format(discarded_key))
                del self.cache_data[discarded_key]
                del self.key_cache[discarded_key]

    def get(self, key):
        """ Gets an item by key
        """
        if key and key in self.cache_data.keys():
            if not self.key_cache:
                self.key_cache[key] = 0
            else:
                self.key_cache[key] = max(list(self.key_cache.values())) + 1

            return self.cache_data[key]
