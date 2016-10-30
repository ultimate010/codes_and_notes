# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/edit-distance
@Language: Python
@Datetime: 16-06-13 11:01
'''

class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        wLen1 = len(word1)
        wLen2 = len(word2)
        matrix = []
        for i in range(wLen1 + 1):
            matrix.append(range(wLen2 + 1))
        for row in range(wLen1 + 1):
            for col in range(wLen2 + 1):
                if row == 0:
                    matrix[0][col] = col
                elif col == 0:
                    matrix[row][0] = row
                else:
                    if word1[row - 1] == word2[col -1]:
                        matrix[row][col] = matrix[row - 1][col - 1]
                    else:
                        matrix[row][col] = min(matrix[row-1][col], 
                        matrix[row][col-1], matrix[row-1][col-1]) + 1
        return matrix[-1][-1]