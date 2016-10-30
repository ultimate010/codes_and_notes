# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/minimum-adjustment-cost
@Language: Python
@Datetime: 16-07-04 14:49
'''

class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost1(self, A, target):
        # write your code here
        m = len(A)
        dp = [[10000] * 101 for i in range(m + 1)]
        for i in range(101):
            dp[0][i] = 0
        for i in range(1, m + 1):
            for j in range(1, 101):  # prev num is j
                if dp[i - 1][j] != 10000:
                    for k in range(1, 101):
                        if abs(j - k) <= target:
                        # current - prev <= target
                            dp[i][k] = min(dp[i][k], dp[i - 1][j] + abs(k - A[i - 1]))
        
        
        return min(dp[m])
        
        
    def MinAdjustmentCost(self, A, target):
        m = len(A)
        dp = [[sys.maxint] * (101) for i in range(m + 1)]
        def helper(dp, i, j):
            if j < 0 or j > 100:
                return sys.maxint
            return dp[i][j]

        for i in range(101):
            dp[0][i] = 0
            
        for i in range(1, m + 1):
            for j in range(1, 101):
                for k in range(target + 1):
                    dp[i][j] = min(dp[i][j], min(helper(dp, i - 1, j - k), helper(dp, i - 1, j + k)) + abs(j - A[i - 1]))
        # print dp            
        return min(dp[m])