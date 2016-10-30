# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/left-pad
@Language: Python
@Datetime: 16-06-19 09:01
'''

class StringUtils:
    # @param {string} originalStr the string we want to append to
    # @param {int} size the target length of the string
    # @param {string} padChar the character to pad to the left side of the string
    # @return {string} a string
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # Write your code here
        if len(originalStr) >= size:
            return originalStr
        else:
            ret = padChar * (size - len(originalStr)) + originalStr
            return ret