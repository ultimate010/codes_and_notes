# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/divide-two-integers
@Language: Python
@Datetime: 16-06-30 09:00
'''

class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        # Write your code here
        if divisor == 0:
            return 2147483647
        flag = True if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else False
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1
        if flag:
            ans = -ans
        if ans > 2147483647:
            return 2147483647
        return ans