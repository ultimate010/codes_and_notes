# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/merge-k-sorted-lists
@Language: Python
@Datetime: 16-06-14 11:55
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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # use heap to merge
        # put into heap, skip the empty list
        import heapq
        heap = [[lists[i].val, i] for i in range(len(lists)) if lists[i] != None]
        hSize = len(heap)
        heapq.heapify(heap)
        dummy = ListNode(0)
        tail = dummy
        while hSize > 0:
            val, pos = heapq.heappop(heap)
            tail.next = lists[pos]
            tail = tail.next
            lists[pos] = lists[pos].next
            if lists[pos] is None:  # this list is empty 
                hSize -= 1
            else:
                heapq.heappush(heap, [lists[pos].val, pos])
            
        return dummy.next
            
        
    def mergeKLists3(self, lists):
        # merge list two by two
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            p = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    p = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    p = l2
                    l2 = l2.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return dummy.next 
            
        if len(lists) == 0:
            return None
            
        while len(lists) > 1:
            newList = []
            for i in range(0, len(lists) - 1, 2):  # there should care 
                l3 = mergeTwoLists(lists[i], lists[i + 1])
                newList.append(l3)
            if len(lists) % 2 != 0:  # or odd number
                newList.append(lists[-1])
            lists = newList

        return lists[0]
        
        
    def mergeKLists2(self, lists):
        # divide and conquer, change original list, this can work
        if len(lists) == 0:
            return None
        def mergeKListsHelper(lists, start, end):
            if start == end:  # only one list
                return lists[start]
            mid = start + (end - start) / 2
            l1 = mergeKListsHelper(lists, start, mid)
            l2 = mergeKListsHelper(lists, mid + 1, end)
            
            return mergeTwoLists(l1, l2)
        
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            p = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    p = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    p = l2
                    l2 = l2.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return dummy.next
            
        return mergeKListsHelper(lists, 0, len(lists) - 1)
    
    def mergeKLists1(self, lists):
        # write your code here
        # this is a naive sulution, don't change the orginal list, 
        # this will cause tle.
        ret = None
        for tmpP in lists:
            if tmpP == None:  # skip empty list
                continue
            if ret is None:  # first node
                ret = ListNode(tmpP.val)
                tmpP = tmpP.next
            else:
                if tmpP.val < ret.val:  
                    # not the first and cur val small than the ret.val, just put 
                    # in front for the list
                    nNode = ListNode(tmpP.val, ret)
                    ret = nNode
                    tmpP = tmpP.next
                    
            retP = ret
            while tmpP:
                # find the right pos and insert into the ret list
                while retP.next and retP.next.val < tmpP.val:  
                    # because the tmpP is sorted so we can do this
                    retP = retP.next
                
                retP.next = ListNode(tmpP.val, retP.next)  # insert 
                retP = retP.next
                tmpP = tmpP.next
                
        return ret
    
                    
                    
                    
                    