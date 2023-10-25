#!/usr/bin/env python3
""" 5. LFU Caching. """
from base_caching import BaseCaching
from collections import OrderedDict


def get_lfu(cache):
    """ Returns the least frequently used key
    """
    least_frequent = sorted(cache.values())[1]
    for k, v in cache.items():
        if v == least_frequent:
            return k


class LFUCache(BaseCaching):
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
            if key in self.key_cache.keys():
                self.key_cache[key] += 1
            else:
                self.key_cache[key] = 1

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = get_lfu(self.key_cache)

                print('DISCARD: {}'.format(discarded_key))
                del self.cache_data[discarded_key]
                del self.key_cache[discarded_key]

    def get(self, key):
        """ Gets an item by key
        """
        if key and key in self.cache_data.keys():
            self.key_cache[key] += 1
            return self.cache_data[key]
