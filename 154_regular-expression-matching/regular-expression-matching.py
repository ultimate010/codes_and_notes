# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/regular-expression-matching
@Language: Python
@Datetime: 16-07-03 08:50
'''

class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        m = len(s)
        n = len(p)
        if m == 0 and n == 0:
            return True
        if n > 0 and p[0] == '*':
            return False
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # not use 'x*'
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':  # use 'x*'
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        # print dp                        
        return dp[-1][-1]