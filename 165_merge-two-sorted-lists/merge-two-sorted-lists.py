# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/merge-two-sorted-lists
@Language: Python
@Datetime: 16-06-10 08:40
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
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        l3 = None
        head = None
        p = None
        while l1 and l2:
            if l1.val <= l2.val:
                p = l1; l1 = l1.next
            else:
                p = l2; l2 = l2.next
            
            if head is None:  # process list head
                head = p; l3 = p
            else:
                l3.next = p; l3 = p
        p = l1 if l1 is not None else l2
        while p:
            if head is None:
                head = p; l3 = p; p = p.next
            else:
                l3.next = p; l3 = p; p = p.next
    
        return head