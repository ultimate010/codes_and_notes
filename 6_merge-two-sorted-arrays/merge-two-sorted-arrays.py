# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/merge-two-sorted-arrays
@Language: Python
@Datetime: 16-06-16 10:50
'''

class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        ret = []
        m = len(A)
        n = len(B)
        i, j = 0, 0
        while i < m and j < n:
            if A[i] <= B[j]:
                ret.append(A[i])
                i += 1
            else:
                ret.append(B[j])
                j += 1
        while i < m:
            ret.append(A[i])
            i += 1
        while j < n:
            ret.append(B[j])
            j += 1
        return ret