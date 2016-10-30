# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/paint-house
@Language: Python
@Datetime: 16-06-24 10:50
'''

class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
        # Write your code here
        n = len(costs)
        if n == 0:
            return 0
        for i in range(1, n):
            for j in range(3):
                l = costs[i - 1][(j - 1) % 3]
                r = costs[i - 1][(j + 1) % 3]
                costs[i][j] += min(l, r)
        
        return min(costs[-1])