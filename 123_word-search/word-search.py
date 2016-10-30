# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/word-search
@Language: Python
@Datetime: 16-06-24 05:52
'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist3(self, board, word):
        # write your code here
        # Boundary Condition
        if word == []:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        # Visited Matrix
        visited = [[False for j in range(n)] for i in range(m)]
        # DFS
        for i in range(m):
            for j in range(n):
                if self.exist2(board, word, visited, i, j):
                    return True
        return False

    def exist2(self, board, word, visited, row, col):
        m, n = len(board), len(board[0])
        if row < 0 or row >= m or col < 0 or col >= n:
            return False
        if word == '':
            return True
        if board[row][col] == word[0] and not visited[row][col]:
            visited[row][col] = True
            # row - 1, col
            if self.exist2(board, word[1:], visited, row - 1, col) or self.exist2(board, word[1:], visited, row, col - 1) or self.exist2(board, word[1:], visited, row + 1, col) or self.exist2(board, word[1:], visited, row, col + 1):
                return True
            else:
                visited[row][col] = False
        return False
        
        
    def exist(self, board, word):
        # write your code here
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        if len(word) == 0:
            return True
            
        
        def dfs(board, m, n, row, col, word, start, end):
            if word[start] != board[row][col]:
                return False
            if start + 1 == end: # at the end
                return True
            dirX = [-1, 1, 0, 0]  # up down left right
            dirY = [0, 0, -1 , 1]
            board[row][col] = '#'
            for i in range(4):
                nRow = row + dirX[i]
                nCol = col + dirY[i]
                if nRow >= 0 and nRow < m and nCol >= 0 and nCol < n:
                    if dfs(board, m, n, nRow, nCol, word, start + 1, end):
                        return True
            board[row][col] = word[start]
            return False
            
                        
        for row in xrange(m):
            for col in xrange(n):
                if dfs(board, m, n, row, col, word, 0, len(word)):
                    return True
        return False