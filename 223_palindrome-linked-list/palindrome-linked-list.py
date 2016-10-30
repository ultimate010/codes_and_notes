# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/palindrome-linked-list
@Language: Python
@Datetime: 16-06-29 02:14
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        if not head:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:  # one step vs two step
            slow = slow.next
            fast = fast.next.next
        p = slow.next
        slow.next = None
        dummy = ListNode(0)
        while p:
            t = p.next
            p.next = dummy.next
            dummy.next = p
            p = t
        p1, p2 = head, dummy.next
        while p1 and p2 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
        p = dummy.next
        dummy.next = None
        while p:
            t = p.next
            p.next = dummy.next
            dummy.next = p
            p = t
        slow.next = dummy.next
        return p2 == None