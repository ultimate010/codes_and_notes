# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/reverse-linked-list-ii
@Language: Python
@Datetime: 16-06-16 14:36
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
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head:
            return head
        dummy = ListNode(0)
        # find the start node
        np = dummy
        p = head
        nm = m
        while nm > 1:
            nm -= 1
            np.next = p
            np = p
            p = p.next
        tmp = None
        tail = None
        # now p is the head to reverse
        n = n - m + 1
        while n > 0:
            # print n
            # print p.val
            n -= 1
            if not tail:
                tail = p
            tmp = p.next
            p.next = np.next
            np.next = p
            p = tmp
        if tail:
            tail.next = p
        return dummy.next