# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/number-of-airplanes-in-the-sky
@Language: Python
@Datetime: 16-06-29 05:02
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        points = []
        for i in airplanes:
            points.append((i.start, 1))
            points.append((i.end, -1))
        points = sorted(points, 
        cmp=lambda x, y: x[0] - y[0] if x[0] != y[0] else x[1] - y[1])
        m, s = 0, 0
        
        for i in points:
            s += i[1]
            m = max(m, s)
        return m