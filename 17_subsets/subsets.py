# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/subsets
@Language: Python
@Datetime: 16-06-12 12:21
'''

import copy

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        ret = [[]]
        self.dfs(sorted(S), 0, ret, [])
        return ret
        
    def dfs(self, S, start, ret, tmp):
        for i in range(start, len(S)):
            tmp.append(S[i])
            if tmp not in ret:
                ret.append(copy.copy(tmp))
            self.dfs(S, i + 1, ret, tmp)
            tmp.pop()