# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/simplify-path
@Language: Python
@Datetime: 16-06-30 09:37
'''

class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        # Write your code here
        tmp = path.split('/')
        stack = []
        for i in tmp:
            if i == '':
                continue
            elif i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        t = map(str, stack)
        return '/' + '/'.join(t)