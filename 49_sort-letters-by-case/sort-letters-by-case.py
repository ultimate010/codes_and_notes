# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/sort-letters-by-case
@Language: Python
@Datetime: 16-06-22 12:44
'''

class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        n = len(chars)
        low = 0
        while low < n and chars[low] >= 'a' and chars[low] <= 'z':
            low += 1
        if low == n:
            return 
        high = n - 1
        while low < high:
            while low < high and chars[high] >= 'A' and chars[high] <= 'Z':
                high -= 1
            chars[low], chars[high] = chars[high], chars[low]
            while low < high and chars[low] >= 'a' and chars[low] <= 'z':
                low += 1
            chars[low], chars[high] = chars[high], chars[low]