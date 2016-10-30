# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-increasing-continuous-subsequence
@Language: Python
@Datetime: 16-06-19 05:21
'''

class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if len(A) == 0:
            return 0
        l = [0] * len(A)
        r = [0] * len(A)
        for pos, a in enumerate(A):
            if pos == 0:
                l[0] = 1
                continue
            if A[pos - 1] < a:
                l[pos] = l[pos - 1] + 1
            else:
                l[pos] = 1
                
        for pos in range(len(A) - 1, -1, -1):
            if pos == len(A) - 1:
                r[pos] = 1
                continue
            if A[pos + 1] < A[pos]:
                r[pos] = r[pos + 1] + 1
            else:
                r[pos] = 1
        # print l, r
        
        return max(max(l), max(r))