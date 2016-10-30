# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/unique-characters
@Language: Python
@Datetime: 16-06-18 10:57
'''

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        count = [True] * 256
        for ch in str:
            count[ord(ch)] = not count[ord(ch)]
            if count[ord(ch)]:
                return False
        return True