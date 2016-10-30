# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/majority-number
@Language: Python
@Datetime: 16-06-09 08:43
'''

from collections import defaultdict
class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        preNum = nums[0]
        count = 1
        for pos in range(1, len(nums)):
            if nums[pos] == preNum:
                count += 1
            else:
                count -= 1
                if count == 0:
                    preNum = nums[pos]
                    count = 1
        return preNum
            

    def majorityNumber1(self, nums):
        # write your code here
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1
        for num in hash:
            if hash[num] > (len(nums) / 2):
                return num