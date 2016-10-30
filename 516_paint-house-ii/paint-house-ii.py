# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/paint-house-ii
@Language: Python
@Datetime: 16-06-24 11:15
'''

class Solution:
    # @param {int[][]} costs n x k cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCostII(self, costs):
        # Just remove the last O(n)
        m = len(costs)
        if m == 0:
            return 0
        n = len(costs[0])
        if n == 0:
            return 0
        
        pM, pS, pI = 0, 0, -1
        for i in range(m):
            cM, cS, cI = sys.maxint, sys.maxint, -1
            for j in range(n):
                costs[i][j] += pM if pI != j else pS
                if costs[i][j] < cM:
                    cS = cM
                    cM = costs[i][j]
                    cI = j
                elif costs[i][j] < cS:
                    cS = costs[i][j]
            pM, pS, pI = cM, cS, cI
        return pM
            
            
    def minCostII1(self, costs):
        # Write your code here
        # This straight forward solution O(n^3)
        m = len(costs)
        if m == 0:
            return 0
        n = len(costs[0])
        if n == 0:
            return 0
        for i in range(1, m):
            for j in range(n):
                mv = sys.maxint
                for k in range(n):
                    if k != j:
                        mv = min(mv, costs[i - 1][k])
                costs[i][j] += mv
                
        return min(costs[-1])