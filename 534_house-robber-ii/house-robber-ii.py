# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/house-robber-ii
@Language: Python
@Datetime: 16-07-01 05:07
'''

class Solution:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        # write your code here
        n = len(nums) 
        if n == 0: return 0
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0], dp[1] = 0, nums[1]  #  not chose the first
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        ans = dp[-1]
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        ans = max(ans, dp[-2])
        return ans