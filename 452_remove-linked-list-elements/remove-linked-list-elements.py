# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/remove-linked-list-elements
@Language: Python
@Datetime: 16-06-19 11:26
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        dummy = ListNode(0, head)
        tail = dummy
        while tail and tail.next:
            if tail.next.val == val:
                tail.next = tail.next.next
            else:
                tail = tail.next
        return dummy.next