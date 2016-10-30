# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-list
@Language: Python
@Datetime: 16-06-10 08:48
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
        if head is None or head.next is None:
            return head
        prevP = head; nextP = head.next
        while nextP:
            if nextP.val == prevP.val:  # del this node
                prevP.next = nextP.next;
                nextP = nextP.next
            else:
                prevP = prevP.next
                nextP = nextP.next
        return head