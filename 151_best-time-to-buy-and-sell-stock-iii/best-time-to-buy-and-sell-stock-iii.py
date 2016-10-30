# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii
@Language: Python
@Datetime: 16-06-25 05:32
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        p1 = [0] * n 
        p2 = [0] * n
        curMin = prices[0]
        for i in range(1, n):
            curMin = min(curMin, prices[i])
            p1[i] = max(p1[i - 1], prices[i] - curMin)
        
        curMax = prices[-1]
        for i in range(n - 2, -1 , -1):
            curMax = max(curMax, prices[i])
            p2[i] = max(p2[i + 1], curMax - prices[i])
        ret = 0
        # print p1, p2
        for i in range(n):
            ret = max(ret, p1[i] + p2[i])
        return ret
        
        
    def maxProfit1(self, prices):
        # write your code here
        if not prices:
            return 0
        prev = prices[0]
        ret = []
        for index, p in enumerate(prices):
            if index == 0 or prices[index] >= prices[index - 1]:
                continue
            else:
                ret.append(prices[index - 1] - prev)
                prev = prices[index]
        if p and p > prev:
            ret.append(p - prev)
        ret = sorted(ret)
        print ret
        return sum(ret[-2:])