# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/two-sum
@Language: Python
@Datetime: 16-06-07 06:05
'''

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash = {}
        for pos, num in enumerate(numbers):
            hash[num] = pos + 1
        for pos, num in enumerate(numbers):
            if target - num in hash:
                return [pos + 1, hash[target - num]]