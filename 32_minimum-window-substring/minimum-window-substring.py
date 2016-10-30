# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/minimum-window-substring
@Language: Python
@Datetime: 16-06-16 11:42
'''

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        d, dt = {}, dict.fromkeys(target, 0)
        for c in target: d[c] = d.get(c, 0) + 1
        pi, pj = 0, 0
        count = 0
        ans = ''
        while pj < len(source):
            if source[pj] in d:
                if dt[source[pj]] < d[source[pj]]:
                    count += 1
                dt[source[pj]] += 1
            if count == len(target):  # same char count
                while pi < pj:
                    if source[pi] in dt:
                        if dt[source[pi]] == d[source[pi]]:  # skip the useless 
                            break
                        dt[source[pi]] -= 1
                    pi += 1
                if ans == '' or (pj - pi) < len(ans):  # new ans
                    ans = source[pi:pj + 1]
                dt[source[pi]] -= 1
                pi += 1
                count -= 1
            pj += 1
        return ans