# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/number-of-islands
@Language: Python
@Datetime: 16-06-22 11:01
'''

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 
            if grid[row][col] == 1:
                grid[row][col] = 0
                dfs(row - 1, col)
                dfs(row + 1, col)
                dfs(row, col - 1)
                dfs(row, col + 1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    dfs(i, j)
        return count
        
        
    def numIslands1(self, grid):
        # Write your code here
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        mask = [[False] * n for i in range(m)]
        
        def dfs(grid, row, col):
            dRow = [-1, 1, 0, 0]
            dCol = [0, 0, -1, 1]
            for i in range(4):
                nRow = row + dRow[i]
                nCol = col + dCol[i]
                if canGo(nRow, nCol):
                    mask[nRow][nCol] = True
                    dfs(grid, nRow, nCol)
                    
        def canGo(row, col):
            
            if row >= 0 and row < m and col >= 0 and col < n and \
            grid[row][col] and not mask[row][col]:
                return True
            return False
            
        count = 0
        for i in range(m):
            for j in range(n):
                if canGo(i, j):
                    count += 1
                    mask[i][j] = True
                    dfs(grid, i,j)
                    
        return count