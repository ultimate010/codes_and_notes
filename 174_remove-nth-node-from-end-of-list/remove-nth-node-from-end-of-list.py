# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/remove-nth-node-from-end-of-list
@Language: Python
@Datetime: 16-06-10 08:29
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        listLen = 0; prevP = head
        p = head
        while p:
            listLen += 1; p = p.next
        skipPos = listLen - n
        while skipPos > 1 and prevP.next is not None:
            prevP = prevP.next; skipPos -= 1
        if prevP == head:  # need change the head
            head = head.next
        if prevP.next:
            prevP.next = prevP.next.next
        return head