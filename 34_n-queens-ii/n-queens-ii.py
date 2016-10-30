# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/n-queens-ii
@Language: Python
@Datetime: 16-06-16 11:56
'''

class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        mainDiag = [False for i in range( 2 * n - 1)]  # used diag
        antiDiag = [False for i in range( 2 * n - 1)]  # used antidiag
        columns = [False for i in range(n)]  # used column
        
        global count
        count = 0
        def dfs(row):
            if row == n:
                global count
                count += 1
            for col in range(n):
                if columns[col] or mainDiag[row - col + n -1] or \
                antiDiag[row + col]:  # invalid
                    continue 
                else:
                    columns[col] = True
                    mainDiag[row - col + n - 1] = True
                    antiDiag[row + col] = True
                    dfs(row + 1)
                    columns[col] = False
                    mainDiag[row - col + n - 1] = False
                    antiDiag[row + col] = False
        dfs(0)
        return count
