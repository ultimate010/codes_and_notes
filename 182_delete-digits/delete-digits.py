# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/delete-digits
@Language: Python
@Datetime: 16-06-10 05:53
'''

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        if len(A) == 0 or k == len(A):
            return ''
        stack = []
        deleted = 0
        for i in range(len(A)):
            cur = int(A[i])
            while len(stack) > 0 and deleted < k and cur < stack[-1]:
                deleted += 1
                stack.pop()
            stack.append(cur)
            
        while deleted < k:
            deleted += 1
            stack.pop()
        ret = ''
        while len(stack) > 0:
            ret = str(stack.pop()) + ret
        while len(ret) > 1 and ret[0] == '0':
            ret = ret[1:]
        return ret
        
    
    def DeleteDigits1(self, A, k):
        # write you code here
        if len(A) == 0 or k == len(A):
            return ''
        # dp method to solve this
        # (m, n) = min((m-1, n-1), (m-1, n))
        # min(del current, or del before)
        matrix = []
        for i in range(len(A)):
            matrix.append(range(k + 1))
        for row in range(len(A)):
            for col in range(k + 1):
                if col == 0:
                    matrix[row][col] = int(A[:row+1])
                elif row < col:
                    matrix[row][col] = 0
                else:
                    matrix[row][col] = min(matrix[row-1][col-1],
                                           int(A[row:row+1]) +
                                           matrix[row-1][col] * 10)
        # print matrix
        return str(matrix[len(A) - 1][k])