# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/wood-cut
@Language: Python
@Datetime: 16-06-07 13:55
'''

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if len(L) == 0:
            return 0
        shortestL = max(L)
        res = 0
        begin = 1
        end = shortestL
        while begin < end:
            middle = (begin + end) / 2 
            # print middle, begin, end
            
            tk = 0
            for l in L:
                tk += l / middle
            if tk < k:
                end = middle - 1
            else:
                begin = middle + 1
                if res < middle:
                    res = middle
        tk = 0 
        for l in L:
            tk += l / begin
        if tk >= k:
            return begin if begin > res else res
        else:
            return res