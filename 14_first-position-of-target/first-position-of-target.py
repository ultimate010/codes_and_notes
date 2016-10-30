# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/first-position-of-target
@Language: Python
@Datetime: 16-06-07 13:32
'''

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        begin = 0
        end = len(nums) - 1
        while begin < end:
            middle = (begin + end) / 2
            if nums[middle] == target:
                while middle > begin and nums[middle] == nums[middle - 1]:
                    middle -= 1
                return middle
            elif nums[middle] < target:
                begin = middle + 1
            else:
                end = middle - 1
        if nums[begin] == target:
            return begin
        return -1