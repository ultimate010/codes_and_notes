# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/word-ladder
@Language: Python
@Datetime: 16-06-12 13:24
'''

from collections import deque
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    visited = {}
    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end:
            return 1
        
        newWords = deque(self.buildNewWords(start, end, dict, 2))
        while len(newWords) > 0:  # bfs
            w, l = newWords.popleft()
            if w == end:
                return l
            newWords.extend(self.buildNewWords(w, end, dict, l + 1))
            
        
    def buildNewWords(self, start, end, dict, level):
        ret = []
        for pos in range(len(start)):
            for i in range(26):
                nch = chr(ord('a') + i)
                if start[pos] == nch:  #skip same char
                    continue
                newWord = start[:pos] + nch + start[pos+1:]  # new word
                if newWord in self.__class__.visited or \
                    (newWord not in dict and newWord != end):
                    continue
                ret.append((newWord, level))
                self.__class__.visited[newWord] = 1
        return ret