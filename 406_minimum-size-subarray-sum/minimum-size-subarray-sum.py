# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/minimum-size-subarray-sum
@Language: Python
@Datetime: 16-06-30 11:05
'''

class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        n = len(nums)
        if n == 0: return -1
        total, l, r = 0, 0, 0 
        ans = n + 1
        while r < n:
            while r < n and total < s:
                total += nums[r]
                r += 1
            if total < s:
                break
            while l < n and total >= s:
                total -= nums[l]
                l += 1
            ans = min(ans, r - l + 1)
        return -1 if ans == n + 1 else ans
        
    def minimumSizeBug(self, nums, s):
        nums = sorted(nums)
        n = len(nums)
        ss = 0
        for i in range(n - 1, -1, -1):
            ss += nums[i]
            if ss >= s:
                return n - i
        return -1
        
    def minimumSize1(self, nums, s):
        # write your code here
        
        n = len(nums)
        if n == 0:
            return -1
        sums = [0] * (n + 1)
        m = sys.maxint
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        for i in range(n):
            for j in range(i + 1, n + 1):
                if j - i > m:
                    break
                diff = sums[j] - sums[i]
                if diff >= s:
                    m = min(m, j - i)
        return -1 if m == sys.maxint else m