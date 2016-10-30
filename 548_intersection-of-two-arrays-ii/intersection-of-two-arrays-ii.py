# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/intersection-of-two-arrays-ii
@Language: Python
@Datetime: 16-06-19 09:18
'''

class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        hash = {}
        for n in nums1:
            hash[n] = hash.get(n, 0) + 1
        ret = []
        for n in nums2:
            if hash.get(n, 0) > 0:
                hash[n] -= 1
                ret.append(n)
        return ret
        