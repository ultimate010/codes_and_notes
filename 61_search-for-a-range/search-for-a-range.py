# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/search-for-a-range
@Language: Python
@Datetime: 16-06-08 01:21
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        begin = 0
        end = len(A) - 1
        while begin <= end:
            middle = (begin + end) / 2 
            if A[middle] == target:
                # find left and right
                left, right = middle, middle
                while left > 0 and A[left - 1] == A[left]:
                    left -= 1
                while right < len(A) - 1and A[right + 1] == A[right]:
                    right += 1
                return [left, right]
            elif A[middle] < target:
                begin = middle + 1
            else:
                end = middle - 1
        return [-1, -1]