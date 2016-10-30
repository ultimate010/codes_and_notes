# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/minimum-subarray
@Language: Python
@Datetime: 16-06-16 15:04
'''

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        sums = [nums[0] for i in range(len(nums))]
        for i in range(1, len(nums)):
            sums[i] = min(sums[i-1] + nums[i], nums[i])
        return min(sums)