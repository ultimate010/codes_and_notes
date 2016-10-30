# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/flatten-nested-list-iterator
@Language: Python
@Datetime: 16-06-29 06:26
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque
class NestedIterator1(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.queue = deque()
        for i in nestedList:
            self.queue.append(i)
                    
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        t = self.queue.popleft()
        return t.getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.queue: 
            t = self.queue.popleft()
            if t.isInteger():
                self.queue.appendleft(t)
                return True
            else:
                for i in reversed(t.getList()):
                    self.queue.appendleft(i)
        return False
        
class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.queue = deque()
        def dfs(l):
            if l.isInteger():
                self.queue.append(l.getInteger())
            else:
                for i in l.getList():
                    dfs(i)
        for i in nestedList:
            dfs(i)
                    
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.queue.popleft()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        return len(self.queue) > 0
        


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())