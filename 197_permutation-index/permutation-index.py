# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/permutation-index
@Language: Python
@Datetime: 16-06-19 02:39
'''

class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        ret = 1
        factor = 1
        for i in range(len(A) - 2, -1, -1):
            tmp = 0
            for j in range(len(A) - 1, i, -1):
                if A[j] < A[i]:
                    tmp += 1
            ret += factor * tmp
            factor *= len(A) - i
        return ret
        
                
    def permutationIndex1(self, A):
        # Write your code here
        from itertools import permutations
        
        
        for pos, i in enumerate(permutations(sorted(A))):
            
            if i == tuple(A):
                return pos + 1
        return 0