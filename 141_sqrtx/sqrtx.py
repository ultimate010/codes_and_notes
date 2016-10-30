# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/sqrtx
@Language: Python
@Datetime: 16-06-11 11:29
'''

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            middle = (left + right) // 2
            if x / middle > middle:
                left = middle + 1
            elif x / middle < middle:
                right = middle - 1
            else:
                return middle
        return left - 1
    
    def sqrt1(self, x):
        # write your code here
        if x == 0:
            return 0
        for i in xrange(1, x + 1):
            if i*i == x:
                return i
            elif i*i > x:
                return i - 1