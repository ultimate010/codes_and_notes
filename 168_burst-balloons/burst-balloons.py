# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/burst-balloons
@Language: Python
@Datetime: 16-07-03 13:34
'''

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]
 
        def DP(i, j):
            if dp[i][j] > 0: return dp[i][j]
            for x in xrange(i, j + 1):
                dp[i][j] = max(dp[i][j],DP(i, x - 1) + nums[i - 1] * nums[x] * nums[j + 1]+ DP(x + 1, j))
            return dp[i][j]
        return DP(1,n)
        
    def maxCoins(self, nums):
        # Write your code here
        n = len(nums)
        dp = [[0] * (n + 2) for i in range(n + 2)]
        nums = [1] + nums + [1]
        def helper(nums, dp, start, end):
            # print start, end
            if dp[start][end] != 0:
                return dp[start][end]
            
            for i in range(start, end + 1):  # last burst the ith balloon
                dp[start][end] = max(dp[start][end], helper(nums, dp, start, i - 1) + 
                nums[i] * nums[start - 1] * nums[end + 1] + helper(nums, dp, i + 1, end))
            return dp[start][end]
            
        return helper(nums, dp, 1, n)