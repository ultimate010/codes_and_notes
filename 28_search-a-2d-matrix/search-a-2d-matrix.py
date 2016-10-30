# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/search-a-2d-matrix
@Language: Python
@Datetime: 16-06-07 13:25
'''

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        begin = 0
        end = m - 1
        while begin < end:
            middle = (begin + end) / 2
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] < target:
                begin = middle + 1
            else:
                end = middle - 1
                row = begin
        if matrix[begin][0] < target:
            row = begin
        else:
            if begin > 0:
                row = begin - 1
            else:
                return False
                
        begin = 0
        end = n - 1
        while begin < end:
            middle = (begin + end) / 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                begin = middle + 1
            else:
                end = middle - 1
        if matrix[row][begin] == target:
            return True
        return False
