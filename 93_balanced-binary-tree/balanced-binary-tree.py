# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/balanced-binary-tree
@Language: Python
@Datetime: 16-06-11 08:29
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced1(self, root):
        # write your code here
        if root is None:
            return True
        else:
            if abs(self.depth(root.left) - self.depth(root.right)) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self, root):
        if root is None:
            return 0
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1
    
    def comb(self, root):
        if root == None:
            return 0
        l = self.comb(root.left)
        if l == -1:
            return -1
        r = self.comb(root.right)
        if r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1
        
    def isBalanced(self, root):
        if root is None:
            return True
        return self.comb(root) != -1
    