# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/palindrome-partitioning-ii
@Language: Python
@Datetime: 16-06-23 11:02
'''

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        n = len(s)
        f = []  # f[i] means that s[i:n] need minimum f[i] cuts
        p = [[False] * n for x in range(n)]
        for i in range(n + 1):
            f.append(n - 1 - i)  # last one is -1
        for i in range(n - 1, -1, -1):
            # for j in range(n - 1, i, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1]):
                    p[i][j] = True  # s[i:j + 1] is palindrome
                    f[i] = min(f[i], f[j + 1] + 1)
        
        return f[0]