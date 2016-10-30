# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/matrix-zigzag-traversal
@Language: Python
@Datetime: 16-06-18 12:40
'''

class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        # write your code here
        ret = []
        m = len(matrix)
        if m == 0: return ret
        n = len(matrix[0])
        if n == 0: return ret
        for row in range(m + n - 1):
            if row % 2 == 0:
                for i in range(row, -1, -1):
                    if i < m and row - i >= 0 and row - i < n:
                        ret.append(matrix[i][row - i])
            else:
                for i in range(row + 1):
                    if i < m and row - i >= 0 and row - i < n:
                        ret.append(matrix[i][row - i])
        return ret