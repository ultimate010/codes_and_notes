# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/convert-expression-to-reverse-polish-notation
@Language: Python
@Datetime: 16-06-23 11:26
'''

class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
    def convertToRPN(self, expression):
        # write your code here
        def getLevel(ch):
            if ch == '+' or ch == '-':
                return 1
            elif ch == '*' or ch == '/':
                return 2
            return 0
        
        stack = []
        ret = []
        for ch in expression:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    ret.append(stack.pop())
                stack.pop()
            elif ch.isdigit():
                ret.append(ch)
            else:
                while len(stack) > 0 and stack[-1] != '(' and getLevel(stack[-1]) >= getLevel(ch):
                    ret.append(stack.pop())
                stack.append(ch)
        while len(stack) > 0 and stack[-1] != '(':
            ret.append(stack.pop())
        return ret