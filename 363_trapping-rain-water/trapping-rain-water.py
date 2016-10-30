# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/trapping-rain-water
@Language: Python
@Datetime: 16-06-23 13:03
'''

class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        n = len(heights)
        if n == 0:
            return 0
            
        lm, rm = [heights[0]] * n, [heights[-1]] * n
        for i in range(1, n):
            lm[i] = max(lm[i - 1], heights[i])
        for j in range(n - 2, -1, -1):
            rm[j] = max(rm[j + 1], heights[j])
        water = 0
        # print lm, rm
        for i in range(1, n - 1):
            lw = min(lm[i], rm[i]) - heights[i]
            water += lw
        return water