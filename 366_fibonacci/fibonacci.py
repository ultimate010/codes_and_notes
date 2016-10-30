# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/fibonacci
@Language: Python
@Datetime: 16-06-15 06:22
'''

class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci1(self, n):
        # write your code here
        if n <= 1:
            return 0
        if n == 2:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def fibonacci(self, n):
        # write your code here
        if n <= 1:
            return 0
        if n == 2:
            return 1
        prev, pprev = 1, 0
        cur = 2
        tmp = 1
        while cur < n:
            cur += 1
            tmp = prev + pprev
            pprev = prev
            prev = tmp
        return tmp