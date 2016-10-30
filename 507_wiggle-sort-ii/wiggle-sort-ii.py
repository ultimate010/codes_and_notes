# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/wiggle-sort-ii
@Language: Python
@Datetime: 16-07-01 02:36
'''

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        size = len(nums)
        snums = sorted(nums)
        for x in range(1, size, 2) + range(0, size, 2):
            nums[x] = snums.pop()
        
        
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