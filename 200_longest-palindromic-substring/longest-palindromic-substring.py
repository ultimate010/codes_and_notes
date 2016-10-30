# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-palindromic-substring
@Language: Python
@Datetime: 16-06-28 14:08
'''

class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code here
        n = len(s)
        if n <= 1:
            return s
        m = 1
        ret = ''
        for i in range(1, 2*n):  # at least 2 char
            if i & 1 == 1:  # odd
                t = i / 2 
                j = t
            else:  # even
                t = i / 2 - 1
                j = t + 1
            while t >= 0 and j < n and s[t] == s[j]:
                t -= 1
                j += 1
            # print t, j
            if t == i:
                pass  # one char
            else:
                if j - t - 1 > m:
                    m = j - t - 1
                    ret = s[t + 1: j]
        return ret