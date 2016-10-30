# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/spiral-matrix-ii
@Language: Python
@Datetime: 16-06-15 15:10
'''

class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        # Write your code here
        matrix = [range(n) for i in range(n)]
        leftRow, leftCol = 0, 0
        rightRow, rightCol = n - 1, n - 1
        num = 1
        while leftRow < rightRow and leftCol < rightCol:
            for col in range(leftCol, rightCol + 1):
                matrix[leftRow][col] = num
                num += 1
            for row in range(leftRow + 1, rightRow + 1):
                matrix[row][rightCol] = num
                num += 1
            for col in range(rightCol - 1, leftCol, -1):
                matrix[rightRow][col] = num
                num += 1
            for row in range(rightRow, leftRow, -1):
                matrix[row][leftCol] = num
                num += 1
            leftRow += 1
            leftCol += 1
            rightRow -= 1
            rightCol -= 1
        
        if leftRow == rightRow:
            for col in range(leftCol, rightCol + 1):
                matrix[leftRow][col] = num
                num +=1
        else:
            for row in range(leftRow, rightRow + 1):
                matrix[row][leftCol] = num
                num += 1
        return matrix