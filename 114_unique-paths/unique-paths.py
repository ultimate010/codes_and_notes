# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/unique-paths
@Language: Python
@Datetime: 16-06-08 05:33
'''

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        matrix = []
        for i in range(m):
            matrix.append([1 for j in range(n)])
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = matrix[row][col -1] + matrix[row - 1][col]
        return matrix[m - 1][n - 1]