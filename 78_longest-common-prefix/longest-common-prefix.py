# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-common-prefix
@Language: Python
@Datetime: 16-05-19 13:22
'''

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs) == 0:
            return ''
        subStr = strs[0]
        for pos in range(len(subStr)):
            subStr = strs[0][0:pos+1]
            done = False
            for pos in range(1, len(strs)):
                if not strs[pos].startswith(subStr):
                    done = True
                    break
            if done:
                subStr = subStr[:-1]
                break
            
        return subStr