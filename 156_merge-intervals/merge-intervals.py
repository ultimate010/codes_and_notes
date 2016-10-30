# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/merge-intervals
@Language: Python
@Datetime: 16-06-18 10:51
'''



"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        intervals = sorted(intervals, key=lambda x:x.start)
        if len(intervals) <= 1:
            return intervals
        ret = [intervals[0]]
        for pos in range(1, len(intervals)):
            i = intervals[pos]
            prev = ret.pop()
            if prev.end < i.start:
                ret.append(prev)
                ret.append(i)
            else:
                ret.append(Interval(min(prev.start, i.start), 
                max(prev.end,i.end)))
        return ret