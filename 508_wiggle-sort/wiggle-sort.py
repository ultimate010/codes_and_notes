# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/wiggle-sort
@Language: Python
@Datetime: 16-07-01 02:22
'''

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            if (i % 2 == 0 and nums[i] > nums[i - 1]) or (i % 2 != 0 and nums[i] < nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i] 
    
    def wiggleSort1(self, nums):
        # Write your code here
        if not nums:
            return 
        a = sorted(nums)
        mid = len(a) / 2
        l1 = a[:mid]
        l2 = a[mid:]
        i, j = 0, 0
        index = 0
        while i < len(l1) and j < len(l2):
            nums[index] = l1[i]
            index += 1
            i += 1
            nums[index] = l2[len(l2) - 1 - j]
            index += 1
            j += 1
        while i < len(l1):
            nums[index] = l1[i]
            index += 1
            i += 1
        while j < len(l2):
            nums[index] = l2[len(l2) - 1 - j]
            index += 1
            j += 1
        # print nums