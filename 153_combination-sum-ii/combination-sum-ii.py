# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/combination-sum-ii
@Language: Python
@Datetime: 16-06-25 05:51
'''

class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target): 
        # write your code here
        ret = []
        def dfs(A, start, end, path, target, curSum):
            if start > end or curSum > target:
                return 
            path.append(A[start])
            if curSum + A[start] == target:
                if path not in ret:
                    ret.append(path[:])
                path.pop()
                return 
            # chose
            dfs(A, start + 1, end, path, target, curSum + A[start])
            # not chose
            path.pop()
            dfs(A, start + 1, end, path, target, curSum)
            
            
        dfs(sorted(candidates), 0, len(candidates) - 1, [], target, 0)
        return ret