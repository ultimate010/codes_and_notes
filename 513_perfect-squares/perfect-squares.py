# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/perfect-squares
@Language: Python
@Datetime: 16-06-30 15:06
'''

class Solution:
    # @param {int} n a positive integer
    # @return {int} an integer
    def numSquares(self, n):
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        i = 0
        while i * i < n:
            b = int((n - i * i) ** 0.5)
            if b * b + i * i == n:
                if b == 0 and i == 0:
                    return 0
                elif b != 0 and i != 0:
                    return 2
                else:
                    return 1
            i += 1
        return 3
        
    def numSquares1(self, n):
        # Write your code here
        squares = []
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            t = i * i
            if t > n:
                break
            f[t] = 1
            squares.append(t)
        
        def search(f, k):
            if f[k] != 0:
                return f[k]
            m = sys.maxint
            for i in range(len(squares)):
                t = squares[i]
                if k < t:
                    break
                m = min(search(f, k - t), m)
            f[k] = m + 1
            return f[k]
            
        search(f, n)
        return f[n]