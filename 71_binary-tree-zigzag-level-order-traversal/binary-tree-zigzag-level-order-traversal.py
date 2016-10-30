# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-zigzag-level-order-traversal
@Language: Python
@Datetime: 16-06-16 06:24
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
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
        ret = []
        level = []
        flag = True
        from collections import deque
        queue = deque()
        queue.append(root)
        curLen, nextLen = 1, 0
        while len(queue) > 0:
            
            p = queue.popleft()
            curLen -= 1
            if p:
                level.append(p.val)
                queue.append(p.left)
                queue.append(p.right)
                nextLen += 2
            if curLen == 0:
                if len(level) == 0:
                    break
                copy = level[:]
                if not flag:
                    copy.reverse()
                ret.append(copy)
                flag = not flag
                level = []
                curLen, nextLen = nextLen, curLen
        
        return ret