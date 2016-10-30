# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-representation
@Language: Python
@Datetime: 16-06-09 07:36
'''

class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        pos = n.find('.')
        retStr = ''
        decimal = 0
        if pos != -1:
            integer = int(n[0:pos])
            decimal = float('0' + n[pos:])
        else:
            integer = int(n)
        count = 0
        
        while decimal != 0 and count < 32:
            ans = decimal * 2;
            tmp = int(ans);
            retStr += str(tmp)
            decimal = ans - tmp;
            count += 1
        if decimal != 0:
            return 'ERROR'
        if retStr != '': 
            # has decimal, need plus dot
            retStr =  '.' + retStr
        if integer == 0:
            # deal with only decimal
            retStr = '0' + retStr
        while integer != 0:
            retStr = str(integer % 2) + retStr
            integer /= 2
        return retStr