# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/compare-strings
@Language: Python
@Datetime: 16-05-19 12:28
'''

from collections import defaultdict
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        keyDict = defaultdict(int)
        for char in A:
            keyDict[char] += 1
        for char in B:
            keyDict[char] -= 1
        for char in keyDict:
            if keyDict[char] < 0:
                return False
        return True