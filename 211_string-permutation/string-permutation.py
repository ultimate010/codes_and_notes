# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/string-permutation
@Language: Python
@Datetime: 16-06-15 14:12
'''

class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        if len(A) != len(B):
            return False
        hash = {}
        for c in A:
            hash.setdefault(c, 0)
            hash[c] += 1
        for c in B:
            hash.setdefault(c, 0)
            hash[c] -= 1
        for c in hash:
            if hash[c] != 0:
                return False
        return True