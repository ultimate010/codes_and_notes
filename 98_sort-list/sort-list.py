# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/sort-list
@Language: Python
@Datetime: 16-06-11 08:05
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
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        return self.mergeSort(head)
        # return self.quickSort1(head)
        # return self.quickSort(head, None)
    
    def findMiddle(self, head):
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        h3 = l3 = None
        while l1 and l2:
            if l1.val < l2.val:
                h3, l3 = self.insertInto(h3, l3, l1)
                l1 = l1.next
            else:
                h3, l3 = self.insertInto(h3, l3, l2)
                l2 = l2.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return h3
        
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        middle = self.findMiddle(head)
        if middle:  # split the list
            tmpP = middle.next
            middle.next = None
            return self.merge(self.mergeSort(head), self.mergeSort(tmpP))
        else:
            return head
            
    def insertInto(self, head, p, node):
        if head is None:
            head = node; p = node
        else:
            p.next = node; p = node
        return head, p
        
    def quickSort1(self, head):
        if head is None or head.next is None:
            return head
        # at least two node
        h1 = l1 = h2 = l2 = None
        pHead = head.next
        while pHead:
            if pHead.val < head.val:
                h1, l1 = self.insertInto(h1, l1, pHead)
            else:
                h2, l2 = self.insertInto(h2, l2, pHead)
            pHead = pHead.next
        if l2 is not None:
            l2.next = None
        if l1 is not None:
            l1.next = None
        
        h1 = self.quickSort1(h1)  # sort left 
        h2 = self.quickSort1(h2)  # sort right
        l1, l2  = h1, h2
        while l1 and l1.next:
            l1 = l1.next
            
        if l1 is not None:
            l1.next = head
            head.next = h2
            return h1
        else:
            head.next = h2
            return head

    
    def partition(self, head, tail):
        pPrev = head
        pNext = head.next
        # make sure prev ... next is larger than k, 0 ... prev is smaller than k 
        while pNext != tail:
            if pNext.val < head.val:
                # need swap
                pPrev.next.val, pNext.val = pNext.val, pPrev.next.val
                pPrev = pPrev.next
            pNext = pNext.next
        head.val, pPrev.val = pPrev.val, head.val
        return pPrev
        
    def quickSort(self, head, tail):
        if head != tail:
            mid = self.partition(head, tail)  # at least one node
            self.quickSort(head, mid)
            self.quickSort(mid.next, tail)
        return head
