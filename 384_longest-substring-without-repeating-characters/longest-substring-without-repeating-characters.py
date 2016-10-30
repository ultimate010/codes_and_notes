# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-substring-without-repeating-characters
@Language: Python
@Datetime: 16-06-29 02:47
'''

class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        hash = {}
        m = 0
        for i in range(len(s)):
            if s[i] in hash and start <= hash[s[i]]:
                start = hash[s[i]] + 1
            hash[s[i]] = i
            m = max(m, i - start + 1)
        return m
        
    def lengthOfLongestSubstring1(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return 0
        m = 1
        s = s + s[-1]
        for i in range(n):
            hash = {}
            for j in range(i, n + 1):
                if s[j] not in hash:
                    hash[s[j]] = 1
                else:
                    break

            l = j - i
            if l > m:
                m = l
                ret = s[i:j]
                
        return m 