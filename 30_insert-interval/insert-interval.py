# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/insert-interval
@Language: Python
@Datetime: 16-06-16 11:02
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results = []
        # write your code here
        insertPos = 0
        for i in intervals:
            if i.end < newInterval.start:
                results.append(i)
                insertPos += 1
            elif i.start > newInterval.end:
                results.append(i)
            else:
                newInterval.start = min(newInterval.start, i.start)
                newInterval.end = max(newInterval.end, i.end)
        results.insert(insertPos, newInterval)
        return results