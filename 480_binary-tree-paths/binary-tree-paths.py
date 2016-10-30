# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-paths
@Language: Python
@Datetime: 16-06-19 08:25
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        if root is None:
            return []
        ret = []
        path = []
        def helper(root, ret, path):
            if root and not root.left and not root.right: # the leaf
                path.append(root.val)
                s = ''
                for i in path:
                    if s == '':
                        s += str(i)
                    else:
                        s += '->' + str(i)
                ret.append(s)
                path.pop()
            if root is None:
                return 
            path.append(root.val)
            helper(root.left, ret, path)
            helper(root.right, ret, path)
            path.pop()
                
        helper(root, ret, path)
        
        return ret
