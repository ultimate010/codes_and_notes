# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-array-ii
@Language: Python
@Datetime: 16-06-09 11:41
'''

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        i , j = 0, 0
        count = 0
        while j < len(A):
            if j > 0 and A[j] == A[j - 1]:
                if count < 2:
                    A[i] = A[j]
                    i += 1; j += 1; count += 1
                else:
                    j += 1
            else: #new num
                A[i] = A[j]
                i += 1; j += 1; count = 1
        A = A[:i]
        return i