# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/word-search-ii
@Language: Python
@Datetime: 16-06-14 14:52
'''

class Trie:
    def __init__(self):
        self.hasChild = False
        self.isEnd = False
        self.children = {}
    
    def put(self, key):
        if key == '':
            self.isEnd = True
            self.hasChild = True
            return 
        self.hasChild = True
        if key[0] not in self.children:
            self.children[key[0]] = Trie()
        self.children[key[0]].put(key[1:])
        
    def pop(self, key):
        if key == '':
            self.isEnd = False
            self.hasChild = False   # should set in there to make sure backtrace
            return 
        
        if key[0] in self.children:
            self.children[key[0]].pop(key[1:])
            self.hasChild = any([child.hasChild for child in 
            self.children.values()])
            
    
class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
            return []
            
        self.ret = []
        root = Trie()
        for w in words:
            root.put(w)
        self.directionsX = [0, 0, -1 , 1]  # up down left right
        self.directionsY = [-1, 1, 0, 0]
        for r in range(len(board)):
            for c in range(len(board[0])):  # make sure start from every r, c
                self.dfs(root, root, board, r, c, [])
        
        return self.ret
        
    def dfs(self, root, curNode, board, row, col, path):
        if board[row][col] not in curNode.children:  # can not find
            return 
        
        # find char
        path.append(board[row][col])
        
        curNode = curNode.children[board[row][col]]  # next trie node
        if curNode.isEnd:  # is the end of one word
            self.ret.append(''.join(path))
            root.pop(self.ret[-1])  # remove cur word
        
        board[row][col] = '#'  # mark this char as used
        for i in range(4):
            newRow = row + self.directionsX[i]  
            newCol = col + self.directionsY[i]
            if newRow < 0 or newCol < 0 or \
            newRow >= len(board) or newCol >= len(board[0]):
                continue
            self.dfs(root, curNode, board, newRow, newCol, path)
        board[row][col] = path.pop()  # backtrace