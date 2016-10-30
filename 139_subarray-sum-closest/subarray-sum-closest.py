# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/subarray-sum-closest
@Language: Python
@Datetime: 16-06-24 13:07
'''

class Node:
    def __init__(self, v, p):
        self.val = v
        self.pos = p
        
    def __cmp__(self, other):
        if self.val == other.val:
            return self.pos - other.pos
        return self.val - other.val
        
        
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        s = []
        s.append(Node(0, -1))
        sum = 0
        for i, n in enumerate(nums):
            sum += n
            s.append(Node(sum, i))
        s = sorted(s)
        
        minV = sys.maxint
        ans = [0, 0]
        for i in range(len(s) - 1):
            if s[i + 1].val - s[i].val < minV or (s[i + 1].val -  s[i].val == minV and min(s[i + 1].pos, s[i].pos) + 1 < ans[0]):
                minV = s[i + 1].val - s[i].val
                ans[0] = min(s[i + 1].pos, s[i].pos) + 1
                ans[1] = max(s[i + 1].pos, s[i].pos)
        return ans