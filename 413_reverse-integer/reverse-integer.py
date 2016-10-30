# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/reverse-integer
@Language: Python
@Datetime: 16-06-19 05:52
'''

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        so = -(2 ** 31)
        bo = 2 ** 31 - 1
        flag = False
        if n < 0:
            flag = True
            n = -n
        ret = 0
        while n != 0:
            ret *= 10
            ret += n % 10
            n /= 10
        if ret < so or ret > bo:
            return 0
        if flag:
            ret = -ret
        return ret