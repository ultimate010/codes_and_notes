# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/graph-valid-tree
@Language: Python
@Datetime: 16-06-28 07:11
'''

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        root = range(n)
        def find(root, n):
            while root[n] != n:
                root[n] = root[root[n]]
                n = root[n]
            return n
            
        for e in edges:
            p = find(root, e[0])
            q = find(root, e[1])
            if p == q:  # same group
                return False
            root[p] = q
        return len(edges) == n - 1