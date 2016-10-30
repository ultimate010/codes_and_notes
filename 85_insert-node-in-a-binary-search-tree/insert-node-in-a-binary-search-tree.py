# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/insert-node-in-a-binary-search-tree
@Language: Python
@Datetime: 16-06-11 08:39
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
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            root = node
        else:
            p = root
            prev = root
            while p:
                prev = p
                if p.val > node.val:
                    p = p.left
                else:
                    p = p.right
            if prev.val > node.val:
                prev.left = node
            else:
                prev.right = node
        return root