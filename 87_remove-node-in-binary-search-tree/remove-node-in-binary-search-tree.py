# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/remove-node-in-binary-search-tree
@Language: Python
@Datetime: 16-06-12 06:24
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
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def removeNode(self, root, value):
        # write your code here
        if not root:  
            return root
        elif value < root.val:  
            root.left = self.removeNode(root.left, value)  
        elif value > root.val:
            root.right = self.removeNode(root.right, value)  
        elif root.left and root.right: #found  
            right_min = self.findMin(root.right)  
            root.val = right_min.val 
            root.right = self.removeNode(root.right, right_min.val)  
        elif root.left:  
            root = root.left  
        elif root.right:  
            root = root.right  
        else:  
            root = None   
        return root  
    
    def findMin(self, root):
        while root.left:
            root = root.left
        return root