# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-array
@Language: Python
@Datetime: 16-05-19 22:46
'''

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        prePos, resultLen = 0, 1
        for curPos in range(1, len(A)):
            if A[curPos] != A[prePos]:
                A[resultLen] = A[curPos]
                resultLen += 1
                prePos = curPos
        A = A[: resultLen]
        return resultLen 