# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-level-order-traversal-ii
@Language: Python
@Datetime: 16-06-23 06:25
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
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        # write your code here
        ret = []
        from collections import deque
        queue = deque()
        if not root:
            return ret
        queue.append(root)
        curLen, prevLen = 0, 1
        tmp = []
        while len(queue) > 0:
            p = queue.popleft()
            prevLen -= 1
            if p:
                tmp.append(p.val)
                queue.append(p.left)
                queue.append(p.right)
                curLen += 2
            if prevLen == 0:
                if len(tmp) > 0:
                    ret.append(tmp[:])
                prevLen, curLen = curLen, prevLen
                tmp = []
        ret.reverse()
        return ret