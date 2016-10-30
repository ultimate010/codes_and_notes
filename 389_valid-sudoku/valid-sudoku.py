# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/valid-sudoku
@Language: Python
@Datetime: 16-06-19 05:15
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for row in range(9):
            hash = {}
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if hash.get(board[row][col], None):
                    return False
                else:
                    hash[board[row][col]] = 1
                    
        for col in range(9):
            hash = {}
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if hash.get(board[row][col], None):
                    return False
                else:
                    hash[board[row][col]] = 1
        pos = [[0,0], [0, 1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        start = [[0,0], [0,3], [0, 6], [3, 0], [3, 3], [3, 6], [6,0], [6,3], [6,6]]
        for s in start:
            hash = {}
            for p in pos:
                row, col = s[0] + p[0], s[1] + p[1]
                if board[row][col] == '.':
                    continue
                if hash.get(board[row][col], None):
                    return False
                else:
                    hash[board[row][col]] = 1
        return True
