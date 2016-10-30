# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/single-number
@Language: Python
@Datetime: 16-06-09 07:43
'''

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        a = 0
        for n in A:
            a = a ^ n
        return a
    
    def singleNumber1(self, A):
        # write your code here
        
        if len(A) == 0:
            return 0
            
        hash = {}
        for n in A:
            if n in hash:
                del hash[n]
            else:
                hash[n] = 1
        for n in hash:
            return n