# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximal-square
@Language: Python
@Datetime: 16-06-30 13:22
'''

class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        f = [[0] * n for i in range(m)] 
        ans = 0
        for i in range(m): 
            f[i][0] = matrix[i][0]
            ans = max(f[i][0], ans)
        for j in range(n): 
            f[0][j] = matrix[0][j]
            ans = max(f[0][j], ans)
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = 1 + min(f[i - 1][j], f[i - 1][j - 1], f[i][j - 1])
                    ans = max(f[i][j], ans)
                    
        return ans * ans