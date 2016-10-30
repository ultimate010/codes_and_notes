# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-postorder-traversal
@Language: Python
@Datetime: 16-06-15 14:34
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        p = root
        if not p:
            return []
        ret = []
        stack = []
        while p:
            stack.append([p, True])
            p = p.left
        while len(stack) > 0:
            p, flag = stack.pop()
            if flag:  # first time
                stack.append([p, False])
                p = p.right
                while p:
                    stack.append([p, True])
                    p = p.left
            else:
                ret.append(p.val)
        return ret
            
                
    def postorderTraversal1(self, root):
        # write your code here
        if root is None:
            return []
        ret = []
        ret.extend(self.postorderTraversal(root.left))
        ret.extend(self.postorderTraversal(root.right))
        ret.append(root.val)
        return ret