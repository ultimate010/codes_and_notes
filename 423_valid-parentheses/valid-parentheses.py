# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/valid-parentheses
@Language: Python
@Datetime: 16-06-19 06:25
'''

class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        stack = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if t != '(' and c == ')':
                    return False
                if t != '{' and c == '}':
                    return False
                if t != '[' and c == ']':
                    return False
        return len(stack) == 0