# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/gas-station
@Language: Python
@Datetime: 16-06-09 10:43
'''

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        totalCost = 0
        totalGas = 0
        start = 0
        curGas = 0
        for pos, g in enumerate(gas):
            curGas += g
            curGas -= cost[pos]
            totalGas += g
            totalCost += cost[pos]
            if curGas < 0:
                start = pos + 1
                curGas = 0
        if totalGas >= totalCost:
            return start
        return -1
                
            
    def canCompleteCircuit1(self, gas, cost):
        # write your code here
        for pos, g in enumerate(gas):
            currentGas = 0
            failed = False
            for i in range(pos, len(gas)):
                currentGas += gas[i]
                currentGas -= cost[i]
                if currentGas < 0:
                    failed = True
                    break 
            if failed:
                continue
            for i in range(0, pos):
                currentGas += gas[i]
                currentGas -= cost[i]
                if currentGas < 0:
                    failed = True
                    break
            if not failed:
                return pos
        return -1