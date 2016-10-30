# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/climbing-stairs
@Language: Python
@Datetime: 16-06-13 02:48
'''

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <= 0:
            return 1
        states = [1 for i in range(n + 1)]
        for pos in range(1, n + 1):
            prev1, prev2 = states[pos - 1], 0
            if pos - 2 >= 0:
                prev2 = states[pos - 2]
            states[pos] = prev1 + prev2
        return states[-1]