# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/combinations
@Language: Python
@Datetime: 16-06-12 07:02
'''

import copy

class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        # write your code here  
        if n <= k:
            return [range(1, k + 1)]
        self.ret = []
        self.tmp = []
        self.dfs(n, k, 1)
        return self.ret
        
    def dfs(self, n, k, start):
        if k == 0:
            self.ret.append(copy.copy(self.tmp))
        else:
            for i in range(start, n + 1):
                self.tmp.append(i)
                self.dfs(n, k - 1, i + 1)
                self.tmp.pop()