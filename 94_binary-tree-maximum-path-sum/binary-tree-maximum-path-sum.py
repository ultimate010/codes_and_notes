# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-maximum-path-sum
@Language: Python
@Datetime: 16-06-23 08:08
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
    def maxPathSum(self, root):
        # write your code here
        def helper(root):
            if not root:
                return -sys.maxint, 0
            left = helper(root.left)
            right = helper(root.right)
            # use root or just use left or right
            m = max(root.val + left[1] + right[1], left[0], right[0]) 
            n = max(root.val + left[1], root.val + right[1], 0)
            return m, n
            
        n, _ = helper(root)
        return n