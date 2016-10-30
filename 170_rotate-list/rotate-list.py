# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/rotate-list
@Language: Python
@Datetime: 16-06-10 10:16
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        pHead = head
        if pHead is None or pHead.next is None:
            return head
        listLen = 1
        while pHead.next:
            pHead = pHead.next; listLen += 1
        pHead.next = head  # make circle
        skipLen = listLen - (k % listLen)
        pHead = head
        while skipLen > 1:
            skipLen -= 1; pHead = pHead.next
        newHead = pHead.next
        pHead.next = None  # cut off 
        return newHead