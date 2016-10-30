# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/unique-paths-ii
@Language: Python
@Datetime: 16-06-13 02:42
'''

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        rows = len(obstacleGrid)
        if rows == 0:
            return 0
        cols = len(obstacleGrid[0])
        matrix = []
        for i in range(rows):   matrix.append(range(cols))
        noRow, noCol = False, False
        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    if row == 0: noRow = True
                    if col == 0: noCol = True
                    matrix[row][col] = 0
                    continue
                if row == 0 or col == 0:
                    if row == 0 and noRow:
                        matrix[row][col] = 0
                    elif col == 0 and noCol:
                        matrix[row][col] = 0
                    else:
                        matrix[row][col] = 1
                else:
                    matrix[row][col] = matrix[row-1][col] + \
                    matrix[row][col-1]
        return matrix[-1][-1]