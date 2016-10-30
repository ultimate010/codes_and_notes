# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/convert-sorted-list-to-balanced-bst
@Language: Python
@Datetime: 16-06-10 10:55
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        listLen = 0
        pHead = head
        while pHead:
            listLen += 1; pHead = pHead.next
        if listLen == 0:
            return None
        elif listLen == 1:
            return TreeNode(head.val)
        elif listLen == 2:
            h = TreeNode(head.val)
            h.right = TreeNode(head.next.val)
            return h
        else:  # divide into two part
            listLen /= 2
            pTmp = head; count = 1
            while count < listLen:
                count += 1; pTmp = pTmp.next
            
            h = TreeNode(pTmp.next.val)  # middle 
            pNext = pTmp.next.next
            pTmp.next = None
            h.left = self.sortedListToBST(head)  # left 
            h.right = self.sortedListToBST(pNext)  # right
            return h