# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/rotate-string
@Language: Python
@Datetime: 16-06-16 05:10
'''

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
	    # write you code here
	    
	    if len(s) == 0:
	        return 
	    offset %= len(s)
	    tmp = s[-offset:]
	    s[offset:] = s[:-offset]
	    s[:offset] = tmp
	    return 