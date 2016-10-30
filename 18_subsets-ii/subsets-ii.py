# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/subsets-ii
@Language: Python
@Datetime: 16-06-12 12:18
'''

import copy
class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        ret = [[]]
        self.dfs(sorted(S), 0, ret, [])
        return ret
        
    def dfs(self, s, start, ret, tmp):
        for i in range(start, len(s)):
            tmp.append(s[i])
            if tmp not in ret:
                ret.append(copy.copy(tmp))
            self.dfs(s, i + 1, ret, tmp)
            tmp.pop()