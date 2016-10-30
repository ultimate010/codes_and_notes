# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-subarray-ii
@Language: Python
@Datetime: 16-06-17 03:24
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        if len(nums) == 1:
            return nums[1]
        a, amax = nums[:], nums[:]
        for i in range(1, len(nums)):
            a[i] = max(a[i - 1] + nums[i], nums[i])
            amax[i] = max(amax[i-1], a[i])
        b, bmax = nums[:], nums[:]
        for i in range(len(nums) - 2, -1, -1):
            b[i] = max(b[i + 1] + nums[i], nums[i])
            bmax[i] = max(bmax[i + 1], b[i])
        
        ret = float('-inf')
        for i in range(len(nums) - 1):
            # print amax[i], bmax[i+1]
            ret = max(ret, amax[i] + bmax[i + 1])
        return ret

            
    def maxTwoSubArrays1(self, nums):
        # write your code here    
        n = len(nums)
        a = nums[:]
    	aa = nums[:]
        for i in range(1, n):
            a[i] = max(nums[i], a[i-1] + nums[i])
            aa[i] = max(a[i], aa[i-1])
        b = nums[:]
    	bb = nums[:]
        for i in range(n-2, -1, -1):
            b[i] = max(b[i+1] + nums[i], nums[i])
            bb[i] = max(b[i], bb[i+1])
        mx = -65535
        for i in range(n - 1):
            mx = max(aa[i]+b[i+1], mx)

        return mx