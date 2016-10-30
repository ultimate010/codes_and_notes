# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-product-subarray
@Language: Python
@Datetime: 16-06-13 10:44
'''

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        states = [[nums[0], nums[0]] for i in range(len(nums))] 
        # 0 for max, 1 for min
        maxNum = nums[0]
        for pos in range(1, len(nums)):
            states[pos][0] = max(states[pos - 1][0] * nums[pos], 
            states[pos - 1][1] * nums[pos], nums[pos])
            states[pos][1] = min(states[pos - 1][0] * nums[pos], 
            states[pos - 1][1] * nums[pos], nums[pos])
            if states[pos][0] > maxNum:
                maxNum = states[pos][0]
            
        return maxNum