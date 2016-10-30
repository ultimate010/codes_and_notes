# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/create-maximum-number
@Language: Python
@Datetime: 16-07-08 12:17
'''

class Solution:
    # @param {int[]} nums1 an integer array of length m with digits 0-9
    # @param {int[]} nums2 an integer array of length n with digits 0-9
    # @param {int} k an integer and k <= m + n
    # @return {int[]} an integer array
    def maxNumber(self, nums1, nums2, k):
        # Write your code here
        m = len(nums1)
        n = len(nums2)
        ret = []
        for i in range(max(0, k - n), min(k, m) + 1):
            tmp = self.merge(self.getMax(nums1, i), self.getMax(nums2, k - i))
            ret = max(tmp, ret)
        return ret
    
    def getMax(self, A, k):
        ret = []
        m = len(A)
        for i in range(m):
            while ret and len(ret) + m - i > k and ret[-1] < A[i]:
                ret.pop()
            if len(ret) < k:
                ret.append(A[i])
        return ret
        
    def merge(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
    
    def merge1(self, A, B):
        i, j = 0, 0
        a, b = len(A), len(B)
        ret = []
        while i < a and j < b:
            if A[i] < B[j]:
                ret.append(B[j])
                j += 1
            else:
                ret.append(A[i])
                i += 1
        while i < a:
            ret.append(A[i])
            i += 1
        while j < b:
            ret.append(B[j])
            j += 1
            
        return ret