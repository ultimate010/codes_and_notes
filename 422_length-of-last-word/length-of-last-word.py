# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/length-of-last-word
@Language: Python
@Datetime: 16-06-19 06:22
'''

class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        n = len(s)
        ret = 0
        i = 0
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            start = i
            while i < n and s[i] != ' ':
                i += 1
            end = i
            if end - start > 0:
                ret = end - start
        return ret