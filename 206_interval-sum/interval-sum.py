# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/interval-sum
@Language: Python
@Datetime: 16-06-23 13:52
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class SegmentTree:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum
        self.left, self.right = None, None
    
    @classmethod
    def buildTree(cls, start, end, a):
        if start > end:
            return None
        if start == end:
            return SegmentTree(start, end, a[start])

        node = SegmentTree(start, end, a[start])

        mid = (start + end) / 2
        # print start, mid, end
        node.left = cls.buildTree(start, mid, a)
        node.right = cls.buildTree(mid + 1, end, a)
        # print node.left, node.right
        node.sum = node.left.sum + node.right.sum
        return node
        '''
        if start > end:
            return None
        if start == end:
            return SegmentTree(start, end, a[start])
        left = cls.buildTree(start, (start + end) / 2 - 1, a)
        right = cls.buildTree((start + end) / 2, end, a)
        root = SegmentTree(start, end, (left.sum + right.sum))
        root.left = left
        root.right = right
        
        return root
        '''
    
    @classmethod
    def query(cls, root, start, end):
        if not root or root.start > end or root.end < start:
            return 0  # can not find
        if root.start >= start and root.end <= end:
            return root.sum
        return cls.query(root.left, start, end) + cls.query(root.right, \
        start, end)

class Solution:	
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """

            
    def intervalSum(self, A, queries):
        root = SegmentTree.buildTree(0, len(A) - 1, A)
        ret = []
        for q in queries:
            ret.append(SegmentTree.query(root, q.start, q.end))
        return ret
        
        
    def intervalSum1(self, A, queries):
        # write your code here
        ret = []
        for q in queries:
            ret.append(sum(A[q.start:q.end+1]))
        return ret