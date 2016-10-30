# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/generate-parentheses
@Language: Python
@Datetime: 16-06-30 12:18
'''

class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        ret = []
        def dfs(path, l, r, n):
            if r > l or l > n:
                return 
            if r == n:
                ret.append(''.join(path))
                return
                        
            path.append('(')
            dfs(path, l + 1, r, n)
            path.pop()
            path.append(')')
            dfs(path, l, r + 1, n)
            path.pop()            
        
        dfs([], 0, 0, n)
        return ret