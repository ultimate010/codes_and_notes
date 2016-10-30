# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/house-robber
@Language: Python
@Datetime: 16-06-29 05:14
'''

class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        n = len(A)
        if n == 0:
            return 0
        f = [0] * (n + 1)
        f[1] = A[0]
        for i in range(2, n + 1):
            f[i] = max(f[i - 2] + A[i - 1], f[i - 1])
        return f[-1]
        
    
    def houseRobber1(self, A):
        # write your code here
        i, n = 0, len(A)
        ret1 = 0
        ret2 = 0
        while i < n:
            ret1 += A[i]
            if i + 1 < n:
                ret2 += A[i + 1]
            i+=2
            
        return max(ret1, ret2)