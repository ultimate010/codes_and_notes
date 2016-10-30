# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/digit-counts
@Language: Python
@Datetime: 16-06-16 04:53
'''

class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        def countK(num, k):
            count = 0
            if k == 0 and num == 0:
                return 1
            while num > 0:
                if k == num % 10:
                    count += 1
                num = num / 10
            return count
        count = 0
        for num in range(n + 1):
            count += countK(num, k)
        return count