# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/lru-cache
@Language: Python
@Datetime: 16-05-14 15:56
'''

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.cache = []
        self.index = {}

    # @return an integer
    def get(self, key):
        # write your code here
        if self.index.get(key) is None:
            return -1
        else:
            self.cache.remove(key)
            self.cache.append(key)
            return self.index[key]
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if self.index.get(key) is None:
            # add new k v
            self.cache.append(key)
            self.index[key] = value
            if len(self.index) > self.capacity:
                del self.index[self.cache[0]]
                self.cache.remove(self.cache[0])
        else:
            self.cache.remove(key)
            self.cache.append(key)
            self.index[key] = value