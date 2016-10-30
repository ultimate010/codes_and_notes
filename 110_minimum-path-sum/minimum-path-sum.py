# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/minimum-path-sum
@Language: Python
@Datetime: 16-06-18 11:15
'''

class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        matrix = [[0] * (n + 1) for i in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1:
                    matrix[row][col] = matrix[row][col - 1] + grid[row - 1][col - 1] 
                    continue
                if col == 1:
                    matrix[row][col] = matrix[row - 1][col] + grid[row - 1][col - 1] 
                    continue
                matrix[row][col] = min(matrix[row - 1][col], 
                matrix[row][col -1]) + grid[row - 1][col - 1] 
        return matrix[-1][-1]