# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/ugly-number
@Language: Python
@Datetime: 16-06-19 11:57
'''

class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        # Write your code here
        if num <= 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        return num == 1