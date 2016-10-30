# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/count-of-smaller-number-before-itself
@Language: Python
@Datetime: 16-07-06 02:27
'''

class SegmentTree:
    def __init__(self, start, end, count=0):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.count = count
        
    @classmethod
    def buildTree(cls, start, end):
        
        if start > end:
            return None
        if start == end:
            return SegmentTree(start, end)
        root = SegmentTree(start, end)
        mid = start + ((end - start) >> 1)
        root.left = cls.buildTree(start, mid)
        root.right = cls.buildTree(mid + 1, end)
        return root
    
    def sum(self, start, end):
        if self.start > end or self.end < start or start > end:
            return 0
        if start <= self.start and self.end <= end:
            return self.count
        return self.left.sum(start, end) + self.right.sum(start, end)
        
    def inc(self, a):
        
        if self.start == a and self.end == a:
            self.count += 1
            return 
        mid = self.start + ((self.end - self.start) >> 1)
        if a <= mid:
            self.left.inc(a)
        else:
            self.right.inc(a)
        self.count = self.left.count + self.right.count
        
class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    def countOfSmallerNumberII(self, A):
        # write your code here
        
        ret = []
        if len(A) == 0:
            return ret
        root = SegmentTree.buildTree(0, max(A))
        for a in A:
            ret.append(root.sum(0, a - 1))
            root.inc(a)
        return ret