# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/swap-nodes-in-pairs
@Language: Python
@Datetime: 16-06-19 08:07
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        dummy = ListNode(0)
        tail = dummy
        count = 0
        while head:
            count += 1
            tail.next = ListNode(head.val, tail.next)
            if count == 2:
                count = 0
                tail = tail.next.next
            head = head.next
        return dummy.next