# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/trailing-zeros
@Language: Python
@Datetime: 16-06-08 05:42
'''

class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        count = 0
        while n:
            count += n / 5
            n = n / 5
        return count