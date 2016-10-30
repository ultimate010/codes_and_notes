# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/roman-to-integer
@Language: Python
@Datetime: 16-06-30 09:31
'''

class Solution:
    # @param {string} s Roman representation
    # @return {int} an integer
    def romanToInt(self, s):

        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        if s == "":
            return 0
            
        index = len(s) - 2
        sum = ROMAN[s[-1]]
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum
        
    def romanToInt1(self, s):
        # Write your code here
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        prev = None
        ans = 0
        for ch in s:
            if prev is None:
                prev = ch
                if ch in roman:
                    ans += nums[roman.index(ch)]
            else:
                two = prev + ch
                if two in roman:
                    if prev in roman:
                        ans -= nums[roman.index(prev)]
                    ans += nums[roman.index(two)]
                    prev = None
                else:
                    prev = ch
                    if ch in roman:
                        ans += nums[roman.index(ch)]
        return ans