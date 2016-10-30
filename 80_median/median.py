# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/median
@Language: Python
@Datetime: 16-06-16 15:07
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        pos = len(nums) / 2
        if len(nums) % 2 == 0:
            pos = len(nums) / 2 - 1
        return nums[pos]