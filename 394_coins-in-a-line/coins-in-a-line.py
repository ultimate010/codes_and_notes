# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/coins-in-a-line
@Language: Python
@Datetime: 16-06-29 06:41
'''

class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        dp = [0] * (n + 1)
        def search(n, dp):
            if dp[n] != 0:
                return True if dp[n] == 1 else False
            if n == 0:
                dp[n] = 2  # False
            elif n == 1 or n == 2:
                dp[n] = 1  # True
            else:
                if not search(n - 1, dp) or not search(n - 2, dp):
                    dp[n] = 1
                else:
                    dp[n] = 2
            return dp[n] == 1
            
        return search(n , dp)
        
    def firstWillWin1(self, n):
        # write your code here
        return n % 3 != 0