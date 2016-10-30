# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-subarray-difference
@Language: Python
@Datetime: 16-06-22 12:37
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        maxL = [nums[0]] * len(nums)
        curMaxL = nums[0]
        minL = [nums[0]] * len(nums)
        curMinL = nums[0]
        maxR = [nums[-1]] * len(nums)
        curMaxR = nums[-1]
        minR = [nums[-1]] * len(nums)
        curMinR = nums[-1]
        for i in range(1, len(nums)):
            r = len(nums) - 1 - i
            curMaxL = max(curMaxL + nums[i], nums[i])
            maxL[i] = max(maxL[i - 1], curMaxL)
            curMinL = min(curMinL + nums[i], nums[i])
            minL[i] = min(minL[i - 1], curMinL)
            curMaxR = max(curMaxR + nums[r], nums[r])
            maxR[r] = max(maxR[r + 1], curMaxR)
            curMinR = min(curMinR + nums[r], nums[r])
            minR[r] = min(minR[r + 1], curMinR)
        ret = 0
        for i in range(len(nums) - 1):
            t1 = abs(maxL[i] - minR[i + 1])
            t2 = abs(maxR[i + 1] - minL[i])
            ret = max(t1, t2, ret)
        return ret      