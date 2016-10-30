# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/word-break
@Language: Python
@Datetime: 16-06-13 12:02
'''

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0:
            return len(s) == 0
            
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        
        maxLength = max([len(w) for w in dict])
        for i in xrange(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):
                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break
        
        return f[n]