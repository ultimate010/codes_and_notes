# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/continuous-subarray-sum
@Language: Python
@Datetime: 16-06-27 16:13
'''

class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here
        if not A:
            return [0, 0]
        f = A[0]
        start = 0
        ret = [0,0]
        m = f
        for i in range(1, len(A)):
            if m < f:
                ret = [start, i - 1]
                m = f
            if f + A[i] > A[i]:
                #chose a
                f = f + A[i]
            else:
                start = i
                f = A[i]
        if m < f:
            ret = [start, i]
        return ret