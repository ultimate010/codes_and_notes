# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/add-binary
@Language: Python
@Datetime: 16-06-19 05:34
'''

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        a = [int(i) for i in a]
        a.reverse()
        b = [int(i) for i in b]
        b.reverse()
        m, n = len(a), len(b)
        i, j = 0, 0
        carry = 0
        ret = []
        while i < m and j < n:
            t = a[i] + b[j] + carry
            ret.append(t % 2)
            carry = t / 2
            i += 1
            j += 1
        while i < m:
            t = a[i] + carry
            ret.append(t % 2)
            carry = t / 2
            i += 1
        while j < n:
            t = b[j] + carry
            ret.append(t % 2)
            carry = t / 2
            j += 1
        if carry != 0:
            ret.append(carry)
        if len(ret) == 0:
            ret = [0]
        ret.reverse()
        
        return ''.join([str(i) for i in ret])