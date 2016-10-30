# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/reverse-linked-list
@Language: Python
@Datetime: 16-06-10 10:06
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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if head is None or head.next is None:  # only one node
            return head
        prev, next = head, head.next
        while next:
            theNext = next.next
            next.next = prev
            prev = next
            next = theNext
        head.next = None
        return prev