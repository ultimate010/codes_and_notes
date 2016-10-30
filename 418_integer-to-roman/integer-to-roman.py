# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/integer-to-roman
@Language: Python
@Datetime: 16-06-30 09:22
'''

class Solution:
    # @param {int} n The integer
    # @return {string} Roman representation
    def intToRoman(self, n):
        # Write your code here
          
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i = 0
        ret = ''
        while n > 0:
            t = n / nums[i]
            while t > 0:
                t -= 1
                ret += roman[i]
            n %= nums[i]
            i += 1
        return ret