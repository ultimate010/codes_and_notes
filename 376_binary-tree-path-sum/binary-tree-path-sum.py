# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-path-sum
@Language: Python
@Datetime: 16-06-15 14:10
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    
    def binaryTreePathSum(self, root, target):
        # Write your code here
        if root is None:
            return []
        path = []
        ret = []
        def helper(root, target, path):
            if root is None:
                return 
            if root.val == target and root.left is None and root.right is None:
                path.append(root.val)
                ret.append(path[:])  # make copy
                path.pop()
            else:
                path.append(root.val)
                helper(root.left, target - root.val, path)
                helper(root.right, target - root.val, path)
                path.pop()
                
        helper(root, target, path)
        return ret