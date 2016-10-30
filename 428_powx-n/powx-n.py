# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/powx-n
@Language: Python
@Datetime: 16-06-30 08:13
'''

class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        def myP(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            t = myP(x, n / 2)
            if n % 2 == 0:
                return t * t
            else:
                return t * t * x
        if n < 0:
            return 1.0 / myP(x, -n)
        return myP(x, n)
    
        
    def myPow1(self, x, n):
        # Write your code here
        if n == 0:
            return 1
        else:
            ret = 1
            flag = True if n < 0 else False
            n = abs(n)
            for i in range(n):
                if flag:
                    ret /= x
                else:
                    ret *= x
            return ret