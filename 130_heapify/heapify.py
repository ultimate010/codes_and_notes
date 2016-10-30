# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/heapify
@Language: Python
@Datetime: 16-06-24 09:30
'''

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        def shiftUp(A, i, n):
            l = 2 * i + 1
            r = 2 * i + 2
            pos = i
            if l < n:
                if A[l] < A[i]:
                    pos = l
            if r < n:
                if A[r] < A[pos]:
                    pos = r
            if pos != i:
                A[i], A[pos] = A[pos], A[i]
                shiftUp(A, pos, n)
            
        for i in range(len(A) // 2, -1, -1):
            shiftUp(A, i, len(A))
    
    def heapify1(self, A):
        # write your code here
        import heapq
        heapq.heapify(A)