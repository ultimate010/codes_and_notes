# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/kth-smallest-number-in-sorted-matrix
@Language: Python
@Datetime: 16-06-29 13:14
'''

class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        def heapAdd(index, nums, n, i):
            index.append(i)
            nums.append(n)
            n = len(nums) - 1
            while n > 0 and nums[n] < nums[(n - 1) / 2]:
                nums[n], nums[(n - 1) / 2] = nums[(n - 1) / 2], nums[n]
                index[n], index[(n - 1) / 2] = index[(n - 1) / 2], index[n]
                n = (n - 1) / 2
                
        def heapDel(index, nums):  # romove the minimal
            index[0] = index[-1]
            nums[0] = nums[-1] 
            index.pop()
            nums.pop()
            n = 0
            while n * 2 + 1 < len(nums):
                t = n * 2 + 1
                if t + 1 < len(nums) and nums[t] > nums[t + 1]:
                    t += 1
                if nums[t] < nums[n]:
                    nums[t], nums[n] = nums[n], nums[t]
                    index[t], index[n] = index[n], index[t]
                else:
                    break
                n = t
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        if m * n < k:
            return 0
        nums = []
        index = []
        pos = [0] * m
        for i in range(m):
            heapAdd(index, nums, matrix[i][0], i)
        ret = []
        while len(ret) < k:
            ret.append(nums[0])
            i = index[0]
            if pos[i] < n - 1:
                pos[i] += 1
                heapAdd(index, nums, matrix[i][pos[i]], i)
            heapDel(index, nums)    
            
        return ret[-1]