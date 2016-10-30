# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/add-two-numbers
@Language: Python
@Datetime: 16-06-18 11:28
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        carry = 0
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            n = l1.val + l2.val + carry
            tail.next = ListNode(n % 10)
            tail = tail.next
            carry = n / 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            n = l1.val + carry
            tail.next = ListNode(n % 10)
            tail = tail.next
            carry = n / 10
            l1 = l1.next
        
        while l2:
            n = l2.val + carry
            tail.next = ListNode(n % 10)
            tail = tail.next
            carry = n / 10
            l2 = l2.next
        if carry != 0:
            tail.next = ListNode(carry)
        return dummy.next    