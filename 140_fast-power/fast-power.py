# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/fast-power
@Language: Python
@Datetime: 16-06-09 07:15
'''

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        return self.method2(a, b, n)

    def method2(self, a, b, n):
        if n == 0:
            return 1 % b
        ans = 1
        a = a % b
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            n = n / 2
            a = (a * a) % b
        return ans

    
    def method1(self, a, b, n):
        ans = 1
        for i in xrange(n):
            ans = (ans % b) * a
        return ans % b