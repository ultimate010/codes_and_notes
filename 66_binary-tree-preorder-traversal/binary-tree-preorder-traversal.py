# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-preorder-traversal
@Language: Python
@Datetime: 16-06-11 10:53
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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        stack = []
        ret = []
        while root or len(stack) > 0:
            if root:
                ret.append(root.val)
                if root.right:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return ret
        
            
    def preorderTraversal2(self, root):
        # write your code here
        if root is None:
            return []
        ret = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            root = stack.pop()
            ret.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return ret

        
        
    def preorderTraversal1(self, root):
        # write your code here
        if root is None:
            return []
        ret = [root.val]
        ret.extend(self.preorderTraversal(root.left))
        ret.extend(self.preorderTraversal(root.right))
        return ret