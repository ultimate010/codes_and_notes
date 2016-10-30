# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-words
@Language: Python
@Datetime: 16-06-18 10:28
'''

class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        ret = []
        if len(dictionary) == 0:
            return ret
        maxLen = max([len(i) for i in dictionary])
        for d in dictionary:
            if len(d) == maxLen:
                ret.append(d)
        return ret