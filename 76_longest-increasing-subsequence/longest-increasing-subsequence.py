# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-increasing-subsequence
@Language: Python
@Datetime: 16-06-23 07:15
'''

class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        def binSearch(A, k, n):
            l, h = 0, k
            while l + 1 < h:
                m = l + (h - l) / 2
                if A[m] == n:
                    start = m
                elif A[m] < n:
                    l = m
                else:
                    h = m
            if A[l] < n:
                return h
            return l
        
        helper = [-1] * (len(nums) + 1)
        k = 0
        for i in range(0, len(nums)):
            if nums[i] >= helper[k]:
                k += 1
                helper[k] = nums[i]
            else:
                pos = binSearch(helper, k, nums[i])
                helper[pos] = nums[i]
        return k
        
        
                    
    def longestIncreasingSubsequence1(self, nums):
        # write your code here
        count = [1] * len(nums)
        ret = 0
        for i in range(1, len(nums)):
            maxL = 0
            for j in range(i):
                if nums[i] >= nums[j]:
                    maxL = max(maxL, count[j])
            count[i] = maxL + 1
            ret = max(ret, count[i])
        return ret