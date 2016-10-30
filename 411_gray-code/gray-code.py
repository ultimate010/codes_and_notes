# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/gray-code
@Language: Python
@Datetime: 16-06-29 15:23
'''

class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        t = self.grayCode(n - 1)
        ret = t[:]
        for i in reversed(t):
            ret.append((1 << (n - 1)) | i)
        return ret
        
    def grayCode1(self, n):
        # Write your code here
        def b2str(n, bits):
            ret = ''
            while bits > 0:
                bits -= 1
                if n & 1:
                    ret = '1' + ret
                else:
                    ret = '0' + ret
                n >>= 1
            return ret
            
        def str2b(s):
            ret = 0
            for i,c in enumerate(reversed(s)):
                if c == '1':
                  ret += 1 << i
            return ret
                
        if n == 0:
            return [0]
        if n == 1:
            return [str2b('0'), str2b('1')]
        else:
            t = self.grayCode(n - 1)
            z = ['0' + b2str(i, n - 1) for i in t] + ['1' + b2str(i, n - 1) for i in reversed(t)]
            
            return map(str2b, z)