# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/recover-rotated-sorted-array
@Language: Python
@Datetime: 16-06-16 14:43
'''

class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        pos = 0
        while pos < len(nums) - 1:
            if nums[pos] > nums[pos + 1]:
                break
            pos += 1
        # this pos is middle
        nnums = nums[pos + 1:] + nums[:pos + 1]
        for pos, v in enumerate(nnums):
            nums[pos] = v