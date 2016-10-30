# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/sort-integers
@Language: Python
@Datetime: 16-06-19 11:29
'''

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        for i in range(len(A) - 1):
            m = i
            for j in range(i + 1, len(A)):
                if A[j] < A[m]:
                    m = j
            A[m], A[i] = A[i], A[m]