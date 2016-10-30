# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/cosine-similarity
@Language: Python
@Datetime: 16-06-19 08:03
'''

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        # write your code here
        na = len(A)
        nb = len(B) 
        if na == 0 or nb == 0 or na != nb:
            return 2.0
        a = 0
        b = 0
        c = 0
        for i in range(na):
            a += A[i] * B[i]
            b += A[i] * A[i]
            c += B[i] * B[i]
        if b == 0 or c == 0:
            return 2.0
        return a / ((b ** 0.5) * (c ** 0.5))