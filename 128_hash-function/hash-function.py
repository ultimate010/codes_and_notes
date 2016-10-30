# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/hash-function
@Language: Python
@Datetime: 16-06-16 15:13
'''

class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        return ans
        '''
        n = len(key)
        count = 0
        for pos, ch in enumerate(key):
            count += ord(ch) * (33**(n - pos - 1)) % HASH_SIZE
        return count % HASH_SIZE
        '''