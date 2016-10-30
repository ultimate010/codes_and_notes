# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/sort-colors-ii
@Language: Python
@Datetime: 16-06-25 02:54
'''

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        def bSort(A, n, start):
            end = len(A) - 1
            while start < end:
                while start < end and A[start] == n:
                    start += 1
                while start < end and A[end] != n:
                    end -= 1
                A[start], A[end] = A[end], A[start]
            return start
            
        prev = 0
        for i in range(k - 1):
            prev = bSort(colors, i + 1, prev)