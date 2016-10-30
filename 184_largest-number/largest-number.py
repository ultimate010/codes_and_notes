# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/largest-number
@Language: Python
@Datetime: 16-06-09 11:05
'''

class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        strNum = [str(i) for i in num]
        strNum = sorted(strNum, cmp=lambda x, y : cmp(x + y, y + x))
        strNum.reverse()
        # print strNum
        res = ''
        start = True
        for s in strNum:
            if start and s == '0':
                continue
            start = False
            res += s
        if start:
            res = '0'
        return res