# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-subarray
@Language: Python
@Datetime: 16-06-13 09:27
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        sums = [nums[0] for i in range(len(nums))]  # first num
        for pos in range(1, len(nums)):
            sums[pos] = max(sums[pos - 1] + nums[pos], nums[pos])
        return max(sums)