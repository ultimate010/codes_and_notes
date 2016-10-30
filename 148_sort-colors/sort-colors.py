# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/sort-colors
@Language: Python
@Datetime: 16-06-25 02:57
'''

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        def bSort(nums, n, start):
            end = len(nums) - 1
            while start < end:
                while start < end and nums[start] == n:
                    start += 1
                while start < end and nums[end] != n:
                    end -= 1
                if start < end:
                    nums[start], nums[end] = nums[end], nums[start]
            return start
            
        bSort(nums, 1, bSort(nums, 0, 0))
        
    def sortColors1(self, nums):
        # write your code here
        # bubble sort
        n = len(nums)
        for i in range(n - 1):
            maxPos = 0
            for j in range(1, n - i):
                if nums[maxPos] < nums[j]:
                    maxPos = j  # find maxPos
            tmp = nums[maxPos]
            k = maxPos
            
            for k in range(maxPos, n - i - 1):
                nums[k] = nums[k + 1]
            nums[k + 1] = tmp
            