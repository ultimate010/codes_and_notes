# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/minimum-depth-of-binary-tree
@Language: Python
@Datetime: 16-06-18 10:25
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
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            l = sys.maxint
            r = sys.maxint
            if root.left:
                l = self.minDepth(root.left)
            if root.right:
                r = self.minDepth(root.right)
            return min(l, r) + 1