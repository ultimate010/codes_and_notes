# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-consecutive-sequence
@Language: Python
@Datetime: 16-06-14 05:59
'''

class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        hash = {}
        for n in num:
            hash[n] = True
        count = 0
        maxCount = 0
        for n in num:
            if hash[n]:  # not use this num
                hash[n] = False
                count += 1
                # find bigger 
                bn = n + 1
                while bn in hash and hash[bn]:
                    hash[bn] = False
                    count += 1
                    bn += 1
                # find smaller
                sn = n - 1
                while sn in hash and hash[sn]:
                    hash[sn] = False
                    count += 1
                    sn -= 1
                maxCount = maxCount if maxCount > count else count
                count = 0
            else:  # already use
                maxCount = maxCount if maxCount > count else count
                count = 0
        return maxCount
                
    def longestConsecutive1(self, num):
        # write your code here
        nums = sorted(num)
        # print nums
        maxCount = 0
        count = 0
        for pos, n in enumerate(nums):
            if pos == 0:
                count = 1
                maxCount = 1
            else:
                if nums[pos-1] == n:  # skip same num
                    continue
                else:
                    if n - 1 != nums[pos - 1]:  # break the rule
                        maxCount = count if maxCount < count else maxCount
                        count = 1
                    else:
                        count += 1
        maxCount = count if maxCount < count else maxCount
        return maxCount