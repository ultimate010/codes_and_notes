# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/count-and-say
@Language: Python
@Datetime: 16-06-19 06:17
'''

class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        # 1 11 21 1211 111221
        if n == 1:
            return '1'
        prev = '1'
        ret = ''
        while n > 1:
            n -= 1
            count = 1
            start = 0
            for pos in range(1, len(prev)):
                if prev[pos] == prev[pos-1]:
                    count += 1
                else:
                    ret += str(count)
                    ret += prev[start]
                    start = pos
                    count = 1
            ret += str(count)
            ret += prev[start]
            
            prev = ret
            ret = ''
        return prev