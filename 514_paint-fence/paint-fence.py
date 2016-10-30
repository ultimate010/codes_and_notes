# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/paint-fence
@Language: Python
@Datetime: 16-06-22 12:09
'''

class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):
        # Write your code here
        if k == 1 and n > 2:
            return 0
        m = max(3, n + 1)
        dp = [0 for i in range(m)]
        dp[0] = 0
        dp[1] = k
        dp[2] = k * k
        if n <= 2:
            return dp[n]
        for i in range(3, m):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
            
        return dp[-1]