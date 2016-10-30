# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/nth-to-last-node-in-list
@Language: Python
@Datetime: 16-06-18 11:23
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
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        if not head or n == 0:
            return head
        circle = [-1] * n
        pos = 0
        while head:
            circle[pos] = head
            pos += 1
            pos %= n
            head = head.next
        return circle[pos]