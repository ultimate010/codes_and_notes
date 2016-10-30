# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/segment-tree-build-ii
@Language: Python
@Datetime: 16-06-30 13:33
'''

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        # write your code here
        def _build(A, start, end):
            if start > end:
                return None
            elif start == end:
                return SegmentTreeNode(start, end, A[start])
            root = SegmentTreeNode(start, end, 0)
            mid = (start + end) / 2
            root.left = _build(A, start, mid)
            root.right = _build(A, mid + 1, end)
            root.max = max(root.left.max, root.right.max)
            return root
            
        return _build(A, 0, len(A) - 1)