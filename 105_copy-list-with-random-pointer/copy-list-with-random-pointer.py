# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/copy-list-with-random-pointer
@Language: Python
@Datetime: 16-06-10 11:11
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        hash = {}
        pHead = head; count = 0
        newHead = None; pTmp = None
        while pHead:
            hash[pHead] = count  # give every node an id
            if newHead is None:
                newHead = pTmp = RandomListNode(pHead.label); hash[count] = pTmp
            else:
                pTmp.next = RandomListNode(pHead.label); pTmp = pTmp.next
                hash[count] = pTmp
                
            pHead = pHead.next; count += 1
    
        count = 0; pTmp = newHead; pHead = head
        while pHead:
            if pHead.random is None:
                pTmp.random = None
            else:
                pTmp.random = hash[hash[pHead.random]]
            pHead = pHead.next; count += 1; pTmp = pTmp.next
        return newHead