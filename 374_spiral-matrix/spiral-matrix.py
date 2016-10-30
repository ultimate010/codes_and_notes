# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/spiral-matrix
@Language: Python
@Datetime: 16-06-14 13:03
'''

class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        # Write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        lefti, leftj = 0, 0  # i is row j is col
        righti, rightj = len(matrix) - 1, len(matrix[0]) - 1
        ret = []
        while lefti < righti and leftj < rightj:
            for col in range(leftj, rightj + 1):
                ret.append(matrix[lefti][col])
            for row in range(lefti + 1, righti + 1):
                ret.append(matrix[row][rightj])
            for col in range(rightj - 1, leftj - 1, -1):
                ret.append(matrix[righti][col])
            for row in range(righti - 1, lefti, -1):
                ret.append(matrix[row][leftj])
            lefti += 1
            leftj += 1
            righti -= 1
            rightj -= 1
            
        if lefti == righti:
            for col in range(leftj, rightj + 1):
                ret.append(matrix[lefti][col])
        elif leftj == rightj:
            for row in range(lefti, righti + 1):
                ret.append(matrix[row][rightj])
        return ret