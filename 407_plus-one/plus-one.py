# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/plus-one
@Language: Python
@Datetime: 16-06-19 05:27
'''

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        if len(digits) == 0:
            return [1]
        ret = []
        carry = (digits[-1] + 1) / 10
        ret.append((digits[-1] + 1) % 10)
        for i in range(len(digits) - 2, -1, -1):
            # print digits[i], carry
            ret.append((digits[i] + carry) % 10)
            carry = (digits[i] + carry) / 10
        if carry != 0:
            ret.append(carry)
        ret.reverse()    
        return ret