# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/implement-queue-by-two-stacks
@Language: Python
@Datetime: 16-06-14 08:16
'''

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        if len(self.stack2) > 0:
            return self.stack2[-1]
        
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
            
        return self.stack2[-1]

    def pop(self):
        # write your code here
        # pop and return the top element
        if len(self.stack2) > 0:
            return self.stack2.pop()
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        ret = self.stack1.pop()
        return ret