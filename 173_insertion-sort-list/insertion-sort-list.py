# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/insertion-sort-list
@Language: Python
@Datetime: 16-06-18 11:36
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
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(-sys.maxint)
        tail = dummy
        while head:
            if head.val > tail.val: # just insert at the end
                tail.next = ListNode(head.val, tail.next)
                tail = tail.next
                head = head.next
                continue
            p = dummy
            while p and p.next and p.next.val < head.val:  # find insertPos
                p = p.next
            p.next = ListNode(head.val, p.next)
            head = head.next
            
        return dummy.next