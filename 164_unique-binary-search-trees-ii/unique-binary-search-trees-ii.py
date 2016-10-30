# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/unique-binary-search-trees-ii
@Language: Python
@Datetime: 16-06-27 15:12
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        def dfs(start, n):
            if start > n:
                return [None]
            ret = []
            for i in range(start, n + 1):
                left = dfs(start, i - 1)
                right = dfs(i + 1, n)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ret.append(root)
            return ret
            
        return dfs(1, n)