# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/container-with-most-water
@Language: Python
@Datetime: 16-06-27 15:40
'''

class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        l, r = 0 , len(heights) - 1
        ret = 0
        while l < r:
            if heights[l] < heights[r]:
                ret = max(heights[l] * (r - l), ret)
                l += 1
            else:
                ret = max(heights[r] * (r - l), ret)
                r -= 1
        return ret