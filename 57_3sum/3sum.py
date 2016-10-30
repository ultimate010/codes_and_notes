# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/3sum
@Language: Python
@Datetime: 16-06-07 11:53
'''

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res = []
        sNumbers = sorted(numbers)
        for pos, num in enumerate(sNumbers):
            if pos > 0 and num == sNumbers[pos - 1]:
                continue
            start = pos + 1
            end = len(sNumbers) - 1
            while start < end:
                if sNumbers[start] + sNumbers[end] + num == 0:
                    res.append((num, sNumbers[start], sNumbers[end]))
                    # skip
                    start += 1
                    end -= 1
                    while sNumbers[start] == sNumbers[start - 1] and start < end:
                        start += 1
                    while sNumbers[end] == sNumbers[end + 1] and start < end:
                        end -= 1
                elif sNumbers[start] + sNumbers[end] + num > 0:
                    end -= 1
                else:
                    start += 1
        return res