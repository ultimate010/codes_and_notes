# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/coins-in-a-line-ii
@Language: Python
@Datetime: 16-06-29 08:32
'''

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        dp = [0] * (n + 1)
        flag = [False] * (n + 1)
        s = [0] * (n + 1)
        s[n-1] = values[-1]
        ss = values[-1]
        for i in range(n - 2, -1, -1):
            ss += values[i]
            s[i] = s[i + 1] + values[i]
            
        def search(i):
            if flag[i]:
                return dp[i] 
            flag[i] = True
            if i == n:
                dp[i] = 0
            elif i == n - 1:
                dp[i] = values[i]
            elif i == n - 2:
                dp[i] = values[i] + values[i + 1]
            else:  # let other chose the min val
                dp[i] = s[i] - min(search(i + 1), search(i + 2))
            return dp[i]
            
        return search(0) * 2 > ss