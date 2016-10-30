# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/next-permutation-ii
@Language: Python
@Datetime: 16-06-22 14:09
'''

class Solution:
    # @param nums: a list of integer
    # @return: return nothing (void), do not return anything, modify nums in-place instead
    def nextPermutation(self, nums):
        # write your code here
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i + 1:] = sorted(nums[i + 1:])
                    return
        nums[:] = sorted(nums)
        return 