# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/linked-list-cycle
@Language: Python
@Datetime: 16-06-10 11:17
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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head or not head.next:
            return False
        pPrev, pNext = head, head
        while pNext and pNext.next:
            pPrev = pPrev.next; pNext = pNext.next.next
            if pPrev == pNext:
                return True
        return False