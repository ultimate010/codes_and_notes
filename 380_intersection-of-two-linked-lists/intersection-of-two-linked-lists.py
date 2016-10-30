# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/intersection-of-two-linked-lists
@Language: Python
@Datetime: 16-06-16 04:42
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # make circle and then find circle
        if not headA or not headB:
            return None
        p = headA
        while p.next:
            p = p.next
        p.next = headA  # make circle
        
        slow = headB
        fast = headB
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # circle
                p = headB
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p
        return None
        
        
    def getIntersectionNode1(self, headA, headB):
        # Write your code here
        hash = {}
        while headA:
            hash[headA] = True
            headA = headA.next
        while headB:
            if headB in hash:
                return headB
            headB = headB.next
        return None