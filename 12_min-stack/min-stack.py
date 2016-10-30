# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/min-stack
@Language: Python
@Datetime: 16-06-14 10:43
'''

class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minNum = None

    def push(self, number):
        # write yout code here
        if len(self.stack) == 0:
            self.minNum = number
        self.stack.append(number - self.minNum)
        if number - self.minNum < 0:
            self.minNum = number

    def pop(self):
        # pop and return the top item in stack
        n = self.stack.pop()
        if n >= 0:
            return self.minNum + n
        else:
            t = self.minNum
            self.minNum = t - n
            return t

    def min(self):
        # return the minimum number in stack
        return self.minNum