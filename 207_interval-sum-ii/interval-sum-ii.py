# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/interval-sum-ii
@Language: Python
@Datetime: 16-06-24 05:11
'''

class SegmentTree:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.val = value
        self.left, self.right = None, None
        
    @classmethod
    def build(cls, start, end, A):
        if start > end:
            return None
        if start == end:
            return SegmentTree(start, end, A[start])
        root = SegmentTree(start, end, A[start])
        mid = start + (end - start) / 2
        root.left = cls.build(start, mid, A)
        root.right = cls.build(mid + 1, end, A)
        root.val = root.left.val + root.right.val
        return root
    
    @classmethod
    def search(cls, root, start, end):
        if not root or root.start > end or root.end < start:
            return 0
        if root.start >= start and root.end <= end:
            return root.val
        return cls.search(root.left, start, end) + cls.search(root.right, 
        start, end)
        
    @classmethod
    def modify(cls, root, index, value):
        if root is None:
            return 
        if root.start == index and root.end == index:
            root.val = value
            return 
            
        if root.left.end >= index:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        
        root.val = root.left.val + root.right.val
        
class Solution:	
    
    # @param A: An integer list
    def __init__(self, A):
        # write your code here
        self.root = SegmentTree.build(0, len(A) - 1, A)
        
    # @param start, end: Indices
    # @return: The sum from start to end
    def query(self, start, end):
        # write your code here
        return SegmentTree.search(self.root, start, end)
    
            
    # @param index, value: modify A[index] to value.
    def modify(self, index, value):
        # write your code here
        return SegmentTree.modify(self.root, index, value)