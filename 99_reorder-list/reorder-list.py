# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/reorder-list
@Language: Python
@Datetime: 16-06-11 02:21
'''

from collections import deque
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
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        queue = deque()
        stack = []
        pHead = head
        listLen = 0
        while pHead:
            queue.append(pHead)
            stack.append(pHead)
            pHead = pHead.next; listLen += 1
        newHead, pNew = None, None
        while len(queue) > listLen / 2 and len(stack) > listLen / 2:
            l = queue.popleft()
            r = stack.pop()
            if l == r:
                if newHead is None:
                    newHead = l; pNew = l
                else:
                    pNew.next = l; l.next = None
                break
            if newHead is None:
                newHead = l; pNew = l
            else:
                pNew.next = l; pNew = l
            pNew.next = r; pNew = r
            pNew.next = None
        if newHead is None:
            return head
        else:
            return newHead
        
    
        
