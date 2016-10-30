# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/happy-number
@Language: Python
@Datetime: 16-06-19 08:30
'''

class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        hash = {}
        while n != 1:
            t = 0
            while n != 0:
                t += (n % 10) ** 2
                n /= 10
            if t in hash:  # loop
                return False
            else:
                hash[t] = 1
            n = t
        return True