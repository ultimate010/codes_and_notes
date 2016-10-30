# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/wildcard-matching
@Language: Python
@Datetime: 16-06-16 07:31
'''

class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        m = len(s)
        n = len(p)
        f = [[False] * (n + 1) for i in range(m + 1)]
        f[0][0] = True
        if m == 0 or p.count('*') == n:
            return True
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = (
                    (f[i-1][j-1]  # s[:i - 1] p[:j - 1] can match
                    and
                    (s[i-1] == p[j-1] or p[j-1] == '?' or p[j-1] == '*')) 
                    # ab ab | ab a? | ab a*
                    or
                    (f[i-1][j] or f[i][j-1]) and p[j-1] == '*' 
                    # 'abcd' 'a*d' cur is 'c' and 'd'
                    )
        return f[-1][-1]
