# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/segment-tree-build
@Language: Python
@Datetime: 16-06-23 13:56
'''

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""

class Solution:	
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end)
        
        root = SegmentTreeNode(start, end)
        mid = (start + end) / 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root