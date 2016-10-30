# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/interval-minimum-number
@Language: Python
@Datetime: 16-06-24 04:27
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class SegmentTree:
    def __init__(self, start, end, minN):
        self.start = start
        self.end = end
        self.minNum = minN
        self.left, self.right = None, None
        
    @classmethod
    def buildTree(cls, start, end, A):
        if start > end:
            return None
        if start == end:
            return SegmentTree(start, end, A[start])
        
        root = SegmentTree(start, end, A[start])
        mid = start + (end - start) / 2
        root.left = cls.buildTree(start, mid, A)
        root.right = cls.buildTree(mid + 1, end, A)
        root.minNum = min(root.left.minNum, root.right.minNum)
        
        return root
        
        
    @classmethod
    def search(cls, root, start, end):
        if not root or root.start > end or root.end < start:
            return sys.maxint
        if root.start >= start and root.end <= end:
            return root.minNum
        
        return min(cls.search(root.left, start, end), \
        cls.search(root.right, start, end))
    

class Solution:	
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        # write your code here
        root = SegmentTree.buildTree(0, len(A) - 1, A)
        ret = []
        for i in queries:
            ret.append(SegmentTree.search(root, i.start, i.end))
        return ret