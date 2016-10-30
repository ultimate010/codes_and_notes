# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/permutation-sequence
@Language: Python
@Datetime: 16-06-22 14:06
'''

class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """
    def getPermutation(self, n, k):
        def nextPermutation(A):
            for i in range(len(A) - 1, -1, -1):
                for j in range(len(A) - 1, i, -1):
                    if A[i] < A[j]:
                        A[i], A[j] = A[j], A[i]
                        A[i+1:] = sorted(A[i+1:])
                        return A
            return sorted(A)
            
        A = [str(i) for i in range(1, n + 1)]
        while k > 1:
            k -= 1
            A = nextPermutation(A)
        return ''.join(A)