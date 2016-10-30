# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/first-missing-positive
@Language: Python
@Datetime: 16-06-07 05:44
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        return self.method1(A)
        
    def method1(self, A):
        hash = {}
        maxNum = 0
        for num in A:
            hash[num] = 1
            maxNum = maxNum if maxNum >= num else num
        for i in range(1, maxNum + 2):
            if i in hash:
                continue
            else:
                return i