# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/previous-permutation
@Language: Python
@Datetime: 16-06-22 14:26
'''

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, num):
        # write your code here
        for i in range(len(num) - 2, -1 , -1):
            if num[i] > num[i + 1]:
                break
        else:
            num.reverse()
            return num
        
        for j in range(len(num) - 1, i, -1):
            if num[j] < num[i]:
                num[j], num[i] = num[i], num[j]
                break
        t = num[i + 1:]
        t.reverse()
        num[i + 1:] = t
        return num