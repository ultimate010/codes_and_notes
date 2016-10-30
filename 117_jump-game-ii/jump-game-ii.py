# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/jump-game-ii
@Language: Python
@Datetime: 16-06-10 07:52
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump2(self, A):
        # dp 
        count = range(len(A))
        count[0] = 0
        for i in range(1, len(A)):
            count[i] = float('inf')
            for j in range(i):
                if j + A[j] >= i:
                    count[i] = min(count[i], count[j] + 1)
                    
        return count[-1]
        
    def jump1(self, A):
        maxJump = 0
        curJump = 0
        count = 0
        for i in range(len(A)):
            if curJump < i:
                count += 1
                curJump = maxJump
            maxJump = max(maxJump, A[i] + i)
        return count
        
    def jump(self, A):
        # write your code here
        target = len(A) - 1
        count = 0
        while target > 0:
            for i in range(target):
                if A[i] + i >= target:
                    count += 1
                    target = i
                    break
        return count