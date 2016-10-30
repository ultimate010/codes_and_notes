# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/next-permutation
@Language: Python
@Datetime: 16-06-10 08:17
'''

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        for i in range(len(num) - 1, -1, -1):
            for j in range(len(num) - 1, i, -1):
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
                    num[i+1:] = sorted(num[i+1:])
                  
                    return num
        num = sorted(num)
        return num
