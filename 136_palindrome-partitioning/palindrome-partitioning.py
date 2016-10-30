# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/palindrome-partitioning
@Language: Python
@Datetime: 16-06-23 10:18
'''

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        def isPalindrome(s):
            for i in range(len(s)):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True
        
        def dfs(s, path):
            if len(s) == 0:  # at the end
                ret.append(path[:])
                
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    path.append(s[:i])
                    dfs(s[i:], path)
                    path.pop()
                    
        ret = []
        dfs(s, [])
        return ret