# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-search-tree-iterator
@Language: Python
@Datetime: 16-06-23 07:30
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.stack = []
        self.p = root

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return self.p or len(self.stack) > 0

    #@return: return next node
    def next(self):
        #write your code here
        while self.p:
            self.stack.append(self.p)
            self.p = self.p.left
        self.p = self.stack.pop()
        ret = self.p
        self.p = self.p.right
        return ret