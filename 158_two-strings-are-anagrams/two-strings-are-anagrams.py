# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/two-strings-are-anagrams
@Language: Python
@Datetime: 16-05-19 12:14
'''

from collections import defaultdict
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        keyDict = defaultdict(int)
        
        for c in s:
            keyDict[c] += 1
        for c in t:
            keyDict[c] -= 1
        for c in keyDict:
            if keyDict[c] != 0:
                return False
        return True