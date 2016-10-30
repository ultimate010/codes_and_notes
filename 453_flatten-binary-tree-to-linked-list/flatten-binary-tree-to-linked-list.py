# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/flatten-binary-tree-to-linked-list
@Language: Python
@Datetime: 16-06-19 08:13
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if root is None or (not root.left and not root.right):
            return root
        
        tp = root.right
        root.right = self.flatten(root.left)
        root.left = None
        p = root
        while p.right:
            p = p.right
        p.right = self.flatten(tp)
        return root