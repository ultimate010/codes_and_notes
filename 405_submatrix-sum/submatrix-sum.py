# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/submatrix-sum
@Language: Python
@Datetime: 16-06-29 14:35
'''

class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        f = [[0] * (n + 1) for i in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                f[row][col] = f[row - 1][col] + f[row][col - 1] - f[row - 1][col - 1] + matrix[row - 1][col - 1]
        ret = [[0, 0],[0, 0]]
        
        for i in range(m):
            for j in range(i + 1, m + 1):
                hash = {}
                for k in range(n + 1):
                    t = f[j][k] - f[i][k]
                    if t in hash:
                        ret[0] = [i, hash[t]]
                        ret[1] = [j - 1, k - 1]
                        return ret
                    else:
                        hash[t] = k 
        return ret