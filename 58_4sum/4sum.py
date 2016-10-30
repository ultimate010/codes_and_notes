# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/4sum
@Language: Python
@Datetime: 16-06-22 14:43
'''

class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        nums = sorted(numbers)
        n = len(nums)
        ret = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = target - nums[i] - nums[j]
                start = j + 1
                end = n - 1
                while start < end:
                    if nums[start] + nums[end] == t:
                        ret.append((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end += 1
                    elif nums[start] + nums[end] < t:
                        start += 1
                    else:
                        end -= 1
        return ret
        
        
    def fourSum1(self ,numbers, target):
        # write your code here
        nums = sorted(numbers)
        n = len(nums)
        ret = set()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for z in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[z] == target:
                            ret.add((nums[i], nums[j], nums[k], nums[z]))
        return list(ret)