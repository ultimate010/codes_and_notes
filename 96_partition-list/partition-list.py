# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/partition-list
@Language: Python
@Datetime: 16-06-10 10:02
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
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        l1 = None; l1Head = None
        l2 = None; l2Head = None
        l3 = head
        while l3:
            if l3.val < x:
                if l1Head is None:
                    l1 = l3; l1Head = l3
                else:
                    l1.next = l3; l1 = l1.next
            else:
                if l2Head is None:
                    l2 = l3; l2Head = l3
                else:
                    l2.next = l3; l2 = l2.next
            t = l3; l3 = l3.next; t.next = None
        if l1Head is None:
            return l2Head
        else:
            l1.next = l2Head
            return l1Head