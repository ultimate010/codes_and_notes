# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/find-peak-element
@Language: Python
@Datetime: 16-06-08 01:04
'''

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        for pos, num in enumerate(A):
            if pos > 0 and pos < len(A) - 1:
                if A[pos - 1] < num and A[pos + 1] < num:
                    return pos