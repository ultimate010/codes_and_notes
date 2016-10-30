# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/intersection-of-two-arrays
@Language: Python
@Datetime: 16-06-19 09:15
'''

class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        hash = {}
        for n in nums1:
            hash[n] = 0
        ret = []
        for n in nums2:
            if hash.get(n, -1) == 0:
                hash[n] = 1
                ret.append(n)
        return ret
        
    def intersection2(self, nums1, nums2):
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        i, j = 0, 0
        nn1, nn2 = len(n1), len(n2)
        ret = []
        while i < nn1 and j < nn2:
            while i < nn1 and n1[i] < n2[j]:
                i += 1
            if i == nn1:
                break
            while j < nn2 and n2[j] < n1[i]:
                j += 1
            if j == nn2:
                break
            if n1[i] == n2[j]:
                if len(ret) > 0 and ret[-1] == n1[i]:
                    pass
                else:
                    ret.append(n1[i])
                    
                i += 1
                j += 1
        return ret
        
    def intersection1(self, nums1, nums2):
        # Write your code here
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1 & s2)