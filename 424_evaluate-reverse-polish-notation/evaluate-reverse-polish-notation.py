# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/evaluate-reverse-polish-notation
@Language: Python
@Datetime: 16-06-30 10:30
'''

class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        # Write your code here
        stack = []
        for t in tokens:
            if t.isdigit() or (len(t) > 1 and t[0] == '-'):
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                if t == '+':
                    stack.append(l + r)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                elif t == '/':
                    stack.append(int(l * 1.0 / r))
        return stack[-1]