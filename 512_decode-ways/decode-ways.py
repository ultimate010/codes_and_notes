# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/decode-ways
@Language: Python
@Datetime: 16-07-01 03:04
'''

class Solution:
    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def numDecodings(self, s):
        # Write your code here
        n = len(s)
        if n == 0: return 0
        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1) :
            if s[i - 1] != '0':
                f[i] = f[i - 1]
            if (int(s[i - 2] + s[i - 1]) >= 10 and int(s[i - 2] + s[i - 1]) <= 26):
                f[i] += f[i - 2]
            
            # if (int(s[i - 2] + s[i - 1]) == 0):
            #     return 0
        return f[-1]