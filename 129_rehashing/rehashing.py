# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/rehashing
@Language: Python
@Datetime: 16-06-24 08:45
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
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        def insertInto(l, v):
            if l is None:
                return ListNode(v)
            p = l
            while p and p.next:  # go to the tail
                p = p.next
            p.next = ListNode(v, p.next)
            return l
                
        # write your code here
        m = len(hashTable)
        n = m * 2
        ret = [None] * n
        for i in range(m):
            p = hashTable[i]
            while p:
                newPos = p.val % n
                ret[newPos] = insertInto(ret[newPos], p.val)
                p = p.next
        return ret