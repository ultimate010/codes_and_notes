# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/n-queens
@Language: Python
@Datetime: 16-06-12 12:06
'''

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    ret = []  # to save result
    queenPos = None  # to save queen position

    def solveNQueens(self, n):
        # write your code here
        self.__class__.queenPos = [-1 for i in range(n)]
        self.__class__.columns = [False for i in range(n)]
        self.__class__.mainDiag = [False for i in range(2 * n - 1)]
        self.__class__.antiDiag = [False for i in range(2 * n - 1)]
        self.dfs(n, 0)  # from 0 row to n row
        
        return self.__class__.ret
    
    def buildResult(self, n):
        ret = []
        for row in range(n):
            tmp = ['.' for i in range(n)]
            tmp[self.__class__.queenPos[row]] = 'Q'
            ret.append(''.join(tmp))
            
        self.__class__.ret.append(ret)
            
    def dfs(self, n, row):
        if row == n:  # find a result
            self.buildResult(n)    
        else:
            for col in range(n):
                # if not self.isValid(row):
                if self.__class__.columns[col] or \
                self.__class__.mainDiag[row - col + n - 1] or \
                self.__class__.antiDiag[row + col]:
                    continue
                else:
                    self.__class__.queenPos[row] = col
                    self.__class__.columns[col] = True
                    self.__class__.mainDiag[row - col + n - 1] = True
                    self.__class__.antiDiag[row + col] = True
                    self.dfs(n, row + 1)
                    self.__class__.queenPos[row] = -1  # backtrace
                    self.__class__.columns[col] = False
                    self.__class__.mainDiag[row - col + n - 1] = False
                    self.__class__.antiDiag[row + col] = False
                    
    def isValid(self, row):
        for i in range(row):
            if self.__class__.queenPos[i] == self.__class__.queenPos[row]:
                # same column
                return False
            if abs(row - i) == abs(self.__class__.queenPos[i] - \
            self.__class__.queenPos[row]):
                    # same diag
                    return False
        return True