# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/expression-evaluation
@Language: Python
@Datetime: 16-06-28 05:45
'''

class Solution:
    # @param expression: a list of strings;
    # @return: an integer
    def evaluateExpression(self, expression):
        # write your code here
        def getLevel(c):
            if c == '+' or c == '-':
                return 1
            else:
                return 2
                
        def convertToRPN(exp):
            ret = []
            stack = []
            for c in exp:
                if c.isdigit():
                    ret.append(c)
                elif c == '(':
                    stack.append(c)
                elif c == ')':
                    while stack and stack[-1] != '(':
                        ret.append(stack.pop())
                    stack.pop()
                else:
                    # + - * /
                    while stack and getLevel(stack[-1]) >= getLevel(c) and stack[-1] != '(':
                        ret.append(stack.pop())
                    stack.append(c)    
            while stack:
                ret.append(stack.pop())
            return ret
            
        def cal(ret):
            stack = [0]
            for c in ret:
                if c.isdigit():
                    stack.append(c)
                elif c == '+':
                    t = int(stack.pop()) + int(stack.pop())
                    stack.append(t)
                elif c == '-':
                    r = int(stack.pop())
                    l = int(stack.pop())
                    t = l - r
                    stack.append(t)
                elif c == '*':
                    r = int(stack.pop())
                    l = int(stack.pop())
                    t = l * r
                    stack.append(t)
                elif c == '/':
                    r = int(stack.pop())
                    l = int(stack.pop())
                    t = l / r
                    stack.append(t)
            return stack[-1]
            
        ret = convertToRPN(expression)
        #  print ret
        sum = cal(ret)
        return sum