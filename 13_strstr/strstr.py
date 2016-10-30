# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/strstr
@Language: Python
@Datetime: 16-05-19 12:24
'''

class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        lenSource, lenTarget = len(source), len(target)
        
        if lenSource == 0 and lenTarget == 0:
            return 0
            
        for startPos in range(lenSource - lenTarget + 1):
            find = True
            for offset in range(lenTarget):
                if source[startPos + offset] != target[offset]:
                    find = False
                    break
            if find:
                return startPos
        
        return -1