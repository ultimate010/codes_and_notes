# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/k-sum
@Language: Python
@Datetime: 16-06-18 08:46
'''

class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
        
    def kSum1(self, A, k, target):
        matrix = [[0] * (target + 1) for i in range(k + 1)]
        matrix[0][0] = 1
        for a in A:
            for i in range(k, 0, -1):
                for j in range(target, a - 1, -1):
                    matrix[i][j] += matrix[i - 1][j - a]
        
        return matrix[k][target]
        
                    
    def kSum(self, A, k, target):
        # write your code here
        matrix = [[[0] * (target + 1) for j in range(k + 1)] for i in range(len(A) + 1)]
        
        for i in range(len(A) + 1):
            matrix[i][0][0] = 1
        
        for i in range(1, len(A) + 1):
            for j in range(1, k + 1):
                for q in range(target + 1):
                    if q - A[i - 1] >= 0:
                        matrix[i][j][q] = matrix[i - 1][j - 1][q - A[i - 1]] + matrix[i - 1][j][q]
                    else:
                        matrix[i][j][q] = matrix[i - 1][j][q]
        # import pprint
        # pprint.pprint(matrix)
        
        return matrix[-1][-1][-1]