# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/search-insert-position
@Language: Python
@Datetime: 16-06-07 12:52
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0:
            return 0
        begin = 0
        end = len(A) - 1
        while begin < end:
            middle = (begin + end) / 2
            
            if A[middle] == target:
                return middle
            elif A[middle] > target:
                end = middle - 1
            else:
                begin = middle + 1
        if A[begin] < target:
            return begin + 1
        else:
            return begin