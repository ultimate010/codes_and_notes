# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/the-smallest-difference
@Language: Python
@Datetime: 16-06-29 02:59
'''

class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        A = sorted(A)
        B = sorted(B)
        i, j = 0, 0
        m = sys.maxint
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                m = min(m, B[j] - A[i])
                i += 1
            else:  # A[i] >= B[j]
                m = min(m, A[i] - B[j])
                j += 1
                
        return m