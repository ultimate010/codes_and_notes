# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/move-zeroes
@Language: Python
@Datetime: 16-06-19 09:05
'''

class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                continue
            nums[i - count] = nums[i]
        for i in range(len(nums) - count, len(nums), 1):
            nums[i] = 0