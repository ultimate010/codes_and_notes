# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/product-of-array-exclude-itself
@Language: Python
@Datetime: 16-06-07 05:27
'''

class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        if len(A) <= 1:
            return [1]
        B = []
        for pos in range(len(A)):
            num = 1
            for i in range(0, pos):
                num *= A[i]
            for j in range(pos + 1, len(A)):
                num *= A[j]
            B.append(num)
        return B