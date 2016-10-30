# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/word-ladder-ii
@Language: Python
@Datetime: 16-06-12 14:23
'''

import copy
from collections import deque
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        def buildpath(path, word):
            if len(prevMap[word])==0:
                path.append(word); currPath=path[:]
                currPath.reverse(); result.append(currPath)
                path.pop();
                return
            path.append(word)
            for iter in prevMap[word]:
                buildpath(path, iter)
            path.pop()
        
        result=[]
        prevMap={}
        length=len(start)
        for i in dict:
            prevMap[i]=[]
        candidates=[set(),set()]; current=0; previous=1
        candidates[current].add(start)
        while True:
            current, previous=previous, current
            for i in candidates[previous]: dict.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            if len(candidates[current])==0: return result
            if end in candidates[current]: break
        buildpath([], end)
        return result
        
    def findLadders1(self, start, end, dict):
        # write your code here
        if start == end:
            return [start]
        ret = []
        tmp = [start, ]
        
        self.minLen = float('inf')
        self.dfs(start, end, dict, ret, tmp, 1)
        # print sorted(ret)
        nRet = []
        for r in ret:
            if len(r) == self.minLen:
                nRet.append(r)
        return nRet
        
        
    def dfs(self, start, end, dict, ret, tmp, level):
        if start == end:  # find a solution
            if len(tmp) <= self.minLen:
                ret.append(copy.copy(tmp))
            if len(tmp) < self.minLen:
                self.minLen = len(tmp)
        else:
            if level >= self.minLen:  # cut off
                return 
            newWords = self.buildNewWords(start, end, tmp, dict)
            
            for n in newWords:
                # print 'chose: ' , n
                tmp.append(n)
                # print 'path' , tmp
                self.dfs(n, end, dict, ret, tmp, level + 1)
                tmp.pop()  # backtrace
            
        
    def buildNewWords(self, start, end, path, dict):
        ret = []
        for pos in range(len(start)):
            for nch in 'abcdefghijklmnopqrstuvwxyz':
                # nch = chr(ord('a') + i)
                if start[pos] == nch:  #skip same char
                    continue
                newWord = start[:pos] + nch + start[pos+1:]  # new word
                if newWord in path or \
                    (newWord not in dict and newWord != end):
                    continue
                
                ret.append(newWord)
        return ret