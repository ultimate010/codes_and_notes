# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/interleaving-positive-and-negative-numbers
@Language: Python
@Datetime: 16-06-25 04:48
'''

class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def rerange(self, A):
        # write your code here
        if not A:
            return 
        countP = 0
        for n in A:
            if n > 0:
                countP += 1
        indexP, indexN = 1, 0
        if countP * 2 > len(A):
            indexP, indexN = 0, 1
        n = len(A)
        while indexP < n and indexN < n:
            while indexP < n and A[indexP] > 0:
                indexP += 2
            while indexN < n and A[indexN] < 0:
                indexN += 2
            if indexP < n and indexN < n:
                A[indexP], A[indexN] = A[indexN], A[indexP]