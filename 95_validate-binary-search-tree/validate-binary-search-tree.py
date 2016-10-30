# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/validate-binary-search-tree
@Language: Python
@Datetime: 16-06-11 11:08
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
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        if root is None:
            return True
        stack = []
        prev = None
        while root or len(stack) > 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                # print root.val
                if prev:
                    if root.val <= prev:
                        return False
                    prev = max(root.val, prev)
                else:
                    prev = root.val
                root = root.right
        return True
        
    
    def isValidBST1(self, root):
        # write your code here
        if root is None:
            return True
        else:
            
            if root.left and self.maxVal(root.left) >= root.val:
                    return False
            
            if root.right and self.minVal(root.right) <= root.val:
                    return False
                    
            return self.isValidBST(root.left) and self.isValidBST(root.right)
    
    def maxVal(self, root):
        if root is None:
            return float('-inf')
        else:
            return max(self.maxVal(root.left), self.maxVal(root.right), root.val)
            
    def minVal(self, root):
        if root is None:
            return float('inf')
        else:
            return min(self.minVal(root.left), self.minVal(root.right), root.val)