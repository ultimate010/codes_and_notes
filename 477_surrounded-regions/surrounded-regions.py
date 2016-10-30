# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/surrounded-regions
@Language: Python
@Datetime: 16-06-30 14:23
'''

class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        def fill(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return 
            queue.append((x, y))
            board[x][y] = '#'
        
        def bfs(x, y):
            if board[x][y] != 'O':
                return 
            fill(x, y)
            
            while queue:
                x, y = queue.pop()
                fill(x + 1, y)
                fill(x - 1, y)
                fill(x, y + 1)
                fill(x, y - 1)
                
        m = len(board)
        if m == 0: return 
        n = len(board[0])
        queue = []
        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)
        for i in range(1, n - 1):
            bfs(0, i)
            bfs(m - 1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'