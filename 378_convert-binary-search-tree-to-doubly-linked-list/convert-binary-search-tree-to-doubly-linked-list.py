# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/convert-binary-search-tree-to-doubly-linked-list
@Language: Python
@Datetime: 16-06-15 14:41
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        dummy = DoublyListNode(0)
        global tail
        tail = dummy
        def helper(root):
            if root is None:
                return 
            helper(root.left)
            global tail
            tail.next = DoublyListNode(root.val)  # add to the end
            tail.next.next = None
            tail = tail.next
            helper(root.right)
        helper(root)
        if dummy.next:
            dummy.next.prev = None
        return dummy.next