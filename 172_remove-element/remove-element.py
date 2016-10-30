# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/remove-element
@Language: Python
@Datetime: 16-05-19 22:40
'''

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        lastPos = 0
        for pos in range(len(A)):
            if A[pos] != elem:
                A[lastPos] = A[pos]
                lastPos += 1
        A = A[: lastPos]
        return lastPos