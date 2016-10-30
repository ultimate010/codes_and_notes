# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/3sum-closest
@Language: Python
@Datetime: 16-06-07 12:36
'''

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        sNumbers = sorted(numbers)
        res = 0
        smallGap = float('inf')
        
        for pos, num in enumerate(sNumbers):
            #skip duplicate num
            if pos > 0 and num == sNumbers[pos - 1]:
                continue
            start = pos + 1
            end = len(sNumbers) - 1
            while start < end:
                sum = num + sNumbers[start] + sNumbers[end] 
                gap = abs(sum - target)
                if gap < smallGap:
                    smallGap = gap
                    res = sum
                if sum < target:
                    start += 1
                else:
                    end -= 1
        return res