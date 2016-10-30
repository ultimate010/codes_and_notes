# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/reverse-words-in-a-string
@Language: Python
@Datetime: 16-06-16 05:01
'''

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        pos = 0
        wstart = 0
        wend = 0
        ret = []
        while pos < len(s):
            while pos < len(s) and s[pos] == ' ':  #skip space
                pos += 1
            if pos >= len(s):
                break
            wstart = pos
            wend = pos + 1
            while wend < len(s) and s[wend] != ' ':  # the word
                wend += 1
            
            ret.append(s[wstart:wend])
            pos = wend
        ret.reverse()
        
        return ' '.join(ret)