# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/space-replacement
@Language: Python
@Datetime: 16-06-15 12:23
'''

class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        ret = ''
        spaceCount = 0
        for pos in range(length):
            if string[pos] == ' ':
                spaceCount += 1
        resultLen = spaceCount * 2 + length
        for pos in range(length - 1, -1, -1):
            if string[pos] == ' ':
                string[pos:pos+3] = '%20'
                spaceCount -= 1
                string[pos+spaceCount * 2:pos+spaceCount * 2 + 3] = string[pos:pos+3]
            else:
                string[pos + spaceCount * 2] = string[pos]
        return resultLen