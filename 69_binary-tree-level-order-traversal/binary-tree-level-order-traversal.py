# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-level-order-traversal
@Language: Python
@Datetime: 16-06-11 15:12
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        curLen, nextLen = 1, 0
        tmp, ret = [], []
        while len(queue) > 0:
            curLen -= 1
            p = queue.popleft()
            if p:
                tmp.append(p.val)
                queue.append(p.left)
                queue.append(p.right)
                nextLen += 2
            if curLen == 0:
                if len(tmp) > 0:
                    ret.append(tmp)
                tmp = []
                curLen, nextLen = nextLen, 0
                
        return ret