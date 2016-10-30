# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-common-substring
@Language: Python
@Datetime: 16-06-22 10:20
'''

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        m = len(A)
        n = len(B)
        if m == 0 or n == 0:
            return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                l = 0
                while i + l < m and j + l < n and A[i + l] == B[j + l]:
                    l += 1
                if l > ans:
                    ans = l
        return ans
        
    
    def longestCommonSubstring2(self, A, B):
        m = len(A)
        n = len(B)
        if m == 0 or n == 0:
            return 0
        dp = [[0] * (n + 1) for i in range(m + 1)]
        maxLen = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxLen = max(dp[i][j], maxLen)
                else:
                    dp[i][j] = 0
        return maxLen
        
    def longestCommonSubstring1(self, A, B):
        # write your code here
        # Brute force
        lenA, lenB = len(A), len(B)
        for subStrLen in range(lenA, 0, -1):   # Please mind the boundary
            for startPos in range(lenA - subStrLen + 1):
                subStr = A[startPos: startPos + subStrLen]
                if B.find(subStr) != -1:
                    return subStrLen
        return 0