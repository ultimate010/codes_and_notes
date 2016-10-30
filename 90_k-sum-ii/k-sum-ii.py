# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/k-sum-ii
@Language: Python
@Datetime: 16-06-23 07:46
'''

class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        # write your code here
        ret = []
        def dfs(A, start, k, target, path):
            if 0 == target and k == 0:
                ret.append(path[:])
                return 
            if target < 0 or k < 0 or start >= len(A):
                return 
            path.append(A[start]) # chose
            dfs(A, start + 1, k - 1, target - A[start], path)
            path.pop()  # not chose
            dfs(A, start + 1, k , target, path)
    
        dfs(A, 0, k, target, [])
        return ret