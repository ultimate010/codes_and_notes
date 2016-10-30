# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/distinct-subsequences
@Language: Python
@Datetime: 16-06-13 11:25
'''

class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        lenS = len(S)
        lenT = len(T)
        f = [0 for i in range(lenT + 1)]
        f[0] = 1
        for row in range(lenS):
            for col in range(lenT - 1, -1, -1):
                if S[row] == T[col]: 
                    f[col + 1] += f[col]
        return f[-1]