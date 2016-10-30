# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-subarray-iii
@Language: Python
@Datetime: 16-06-18 06:59
'''

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        o = -sys.maxint
        matrixLocal = [[o] * (k + 1) for i in range(len(nums) + 1)]
        matrixGlobal = [[o] * (k + 1) for i in range(len(nums) + 1)]
        matrixLocal[0][0] = 0
        matrixGlobal[0][0] = 0
        for i in range(1, len(nums) + 1):
            matrixLocal[i][0] = 0
            matrixGlobal[i][0] = 0
            for j in range(1, k + 1):
                matrixLocal[i][j] = max(matrixLocal[i - 1][j] + nums[i - 1], 
                matrixGlobal[i - 1][j - 1] + nums[i - 1])  
                # continuous or begin new 
                matrixGlobal[i][j] = max(matrixGlobal[i - 1][j], 
                matrixLocal[i][j])
        
        return matrixGlobal[-1][-1]
        
    def maxSubArray1(self, nums, k):
        # write your code here
        oo = 2 ** 32
        n = len(nums)
        f = [[-oo] * (k + 1), [-oo] * (k + 1)]
        g = [[-oo] * (k + 1), [-oo] * (k + 1)]
        
        f[0][0] = 0
        g[0][0] = 0
        for i in range(1, n + 1):
            f[i % 2][0] = 0 
            g[i % 2][0] = 0
            for j in range(1, k + 1):
                f[i % 2][j] = max(f[(i - 1) % 2][j] + nums[i - 1],
                                  g[(i - 1) % 2][j - 1] + nums[i - 1])
                g[i % 2][j] = max(g[(i - 1) % 2][j], f[i % 2][j])
        return g[n % 2][k]