# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/backpack-ii
@Language: Python
@Datetime: 16-06-13 14:07
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
  
        f = [0 for i in range(m + 1)]
        for i in xrange(1, len(A) + 1):
            for j in xrange(m, 0 , -1):
                if j - A[i - 1] >= 0:
                    f[j] = max(f[j], f[j - A[i - 1]] + V[i -1])
                
        return f[-1]  