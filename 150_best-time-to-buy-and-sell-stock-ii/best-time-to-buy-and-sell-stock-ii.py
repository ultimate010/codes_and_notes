# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii
@Language: Python
@Datetime: 16-06-25 05:06
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        ret = 0
        prev = prices[0]
        for index,p in enumerate(prices):
            if index == 0 or prices[index] >= prices[index - 1]:
                continue
            else:
                # print prices[index - 1], prev
                ret += prices[index - 1] - prev
                prev = p
        if p and p > prev:
            ret += p - prev
        return ret