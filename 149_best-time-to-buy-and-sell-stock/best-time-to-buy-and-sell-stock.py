# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock
@Language: Python
@Datetime: 16-06-25 04:52
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        curMin = sys.maxint
        ret = 0
        for p in prices:
            curMin = min(p, curMin)
            ret = max(p - curMin, ret)
        return ret