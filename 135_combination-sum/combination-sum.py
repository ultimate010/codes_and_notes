# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/combination-sum
@Language: Python
@Datetime: 16-06-12 08:28
'''

import copy
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        self.path = []
        self.ret = []
        self.curSum = 0
        self.dfs(sorted(candidates), target)
        return self.ret
        
    def dfs(self, candidates, target):
        for pos, c in enumerate(candidates):
            if pos > 0 and candidates[pos - 1] == candidates[pos]:  # skip same num
                continue
            self.path.append(c)
            self.curSum += c
            
            # print self.curSum, self.path, self.ret
            if self.curSum == target:
                if sorted(copy.copy(self.path)) not in self.ret:
                    self.ret.append(sorted(copy.copy(self.path)))
                self.curSum -= self.path.pop()
            elif self.curSum > target:  # remove this num
                self.path.pop()
                self.curSum -= c
                break
            else:
                self.dfs(candidates, target)
                self.path.pop()
                self.curSum -= c