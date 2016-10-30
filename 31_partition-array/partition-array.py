# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/partition-array
@Language: Python
@Datetime: 16-06-07 08:55
'''

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
        
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        nums.append(None)
        leftPos, rightPos = 0, len(nums) - 1
        while leftPos < rightPos:
            while leftPos < rightPos and nums[leftPos] < k:
                leftPos += 1
            nums[rightPos] = nums[leftPos]
            while leftPos < rightPos and nums[rightPos] >= k:
                rightPos -= 1
            nums[leftPos] = nums[rightPos]
            # print leftPos, rightPos, nums
        nums[leftPos:] = nums[leftPos+1:]

        return leftPos