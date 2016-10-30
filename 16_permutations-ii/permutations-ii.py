# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/permutations-ii
@Language: Python
@Datetime: 16-06-12 12:27
'''

import copy
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        ret = []
        self.dfs(sorted(nums), ret, [])
        return ret
        
    def dfs(self, nums, ret, tmp):
        if len(nums) == 0:
            if tmp not in ret:
                ret.append(copy.copy(tmp))
        else:
            for i in range(len(nums)):
                tmp.append(nums[i])
                newNums = copy.copy(nums)
                newNums = newNums[:i] + newNums[i+1:]  # remove i
                self.dfs(newNums, ret, tmp)
                tmp.pop()
