# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/set-matrix-zeroes
@Language: Python
@Datetime: 16-06-27 14:47
'''

class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        n = len(matrix)
        if not matrix:
            return 
        m = len(matrix[0])
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    for i in range(row):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None
                    for i in range(row + 1, n, 1):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None
                    for i in range(col):
                        if matrix[row][i] != 0:
                            matrix[row][i] = None
                    for i in range(col + 1, m, 1):
                        if matrix[row][i] != 0:
                            matrix[row][i] = None
                        
        for row in range(n):
            for col in range(m):
                if matrix[row][col] is None:
                    matrix[row][col] = 0