# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/letter-combinations-of-a-phone-number
@Language: Python
@Datetime: 16-06-30 11:25
'''

class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        # Write your code here
        map = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        ret = []
        if not digits:
            return ret
        for i in digits:
            tmp = []
            for j in map[i]:
                if len(ret) > 0:
                    for k in ret:
                        tmp.append(k + j)
                else:
                    tmp.append(j)
            ret = tmp[:]
        return ret
        
    def letterCombinations1(self, digits):
        # Write your code here
        map = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        ret = []
        if not digits:
            return ret
        def dfs(map, digits, i, path):
            if i == len(digits):
                ret.append(''.join(path))
                return 
            t = map[digits[i]]
            for k in range(len(t)):
                path.append(t[k])
                dfs(map, digits, i + 1, path)
                path.pop()
                
        dfs(map, digits, 0, [])
        return ret