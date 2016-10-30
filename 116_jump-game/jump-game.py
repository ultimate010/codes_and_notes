# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/jump-game
@Language: Python
@Datetime: 16-06-10 07:26
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        maxPos = 0
        i = 0
        while i < len(A) and i <= maxPos:
            maxPos = max(maxPos, A[i] + i)
            if maxPos >= len(A) - 1:
                return True
            i += 1
        return False