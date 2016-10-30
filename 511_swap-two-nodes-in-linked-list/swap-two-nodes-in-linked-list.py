# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/swap-two-nodes-in-linked-list
@Language: Python
@Datetime: 16-06-24 12:00
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        # Write your code here
                
        def swapAdj(p):
            p1 = p.next
            p2 = p.next.next
            p.next = p2
            tmp = p2.next
            p2.next = p1
            p1.next = tmp
            
        def swapRmt(p1, p2):
            pv1 = p1.next
            pv2 = p2.next
            p1.next = pv2
            tmp = pv2.next
            pv2.next = pv1.next
            p2.next = pv1
            pv1.next = tmp
            
        p1, p2 = None, None
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p and p.next:
            if p.next.val == v1:
                p1 = p
            if p.next.val == v2:
                p2 = p
            p = p.next
        if not p1 or not p2:
            return head
        if p1 == p2:  # same value
            return head
        if p1.next == p2:
            swapAdj(p1)
        elif p2.next == p1:
            swapAdj(p2)
        else:
            swapRmt(p1, p2)
        return dummy.next