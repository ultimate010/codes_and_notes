# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-list-ii
@Language: Python
@Datetime: 16-06-24 10:24
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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(0)
        tail = dummy
        if not head:
            return head
        prev = None
        curCount = 0
        while head:
            if curCount == 0:  # first
                curCount += 1
                prev = head
            else:                
                if prev.val == head.val:
                    curCount += 1
                else:  # new num
                    if curCount == 1:  #only one
                        tail.next = prev
                        tail = prev
                    curCount = 1
                    prev = head
            head = head.next
        if curCount == 1:
            tail.next = prev
            tail = tail.next
        tail.next = None
        return dummy.next