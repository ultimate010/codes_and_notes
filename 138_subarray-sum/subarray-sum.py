# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/subarray-sum
@Language: Python
@Datetime: 16-05-19 19:23
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        for startPos in range(len(nums)):
            sum = nums[startPos]
            if sum == 0:
                return [startPos, startPos]
            for nextPos in range(startPos + 1, len(nums)):
                sum += nums[nextPos]
                if sum == 0:
                    return [startPos, nextPos]
        