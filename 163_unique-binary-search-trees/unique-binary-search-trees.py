# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/unique-binary-search-trees
@Language: Python
@Datetime: 16-06-08 07:27
'''

class Solution:
    # @paramn n: An integer
    # @return: An integer
    hash = {}
    def numTrees(self, n):
        # write your code here
        if n in self.hash:
            return self.hash[n]
        if n == 0:
            return 1
        else:
            count = 0
            for i in range(1, n + 1):
                count += self.numTrees(i - 1) * self.numTrees(n - i)
            self.hash[n] = count
            return count