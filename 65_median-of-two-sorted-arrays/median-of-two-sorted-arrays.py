# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/median-of-two-sorted-arrays
@Language: Python
@Datetime: 16-06-23 06:13
'''

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        def findKth(A, B, k):
            if len(A) == 0:
                return B[k - 1]
            if len(B) == 0:
                return A[k - 1]
            
            if k == 1:
                return min(A[0], B[0])
            
            a = A[k / 2 - 1] if len(A) >= k / 2 else None
            b = B[k / 2 - 1] if len(B) >= k / 2 else None
            if b is None or (a is not None and a < b):
                return findKth(A[k/2:], B, k - k / 2)
            return findKth(A, B[k/2:], k - k / 2)
    
        if (m + n) % 2 == 0:
            s = findKth(A, B, (m + n) / 2)
            b = findKth(A, B, (m + n) / 2 + 1)
            return (s + b) / 2.0
        else:
            return findKth(A, B, (m + n) / 2 + 1)