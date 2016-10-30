# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/subtree
@Language: Python
@Datetime: 16-05-14 12:49
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    
    def isSame(self, T1, T2):
        if T1 is None and T2 is None:
            return True
        if T1 is None or T2 is None:
            return False
        if T1.val != T2.val:
            return False
        return (self.isSame(T1.left, T2.left) and self.isSame(T1.right, T2.right))
        
        
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        '''
        if T2 is None:
            return True
        if T1 is None:
            return False
        t1 =  T1.val == T2.val and self.isSubtree(T1.left, T2.left) and self.isSubtree(T1.right, T2.right)
        if t1:
            return True
        t2 = self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
        return t2
        '''
        if T2 is None:
            return True
        if T1 is None:
            return False
        return self.isSame(T1, T2) or self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
        

        