# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/anagrams
@Language: Python
@Datetime: 16-05-19 12:45
'''

from collections import defaultdict
class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        charSet2List = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string))
            charSet2List[key].append(string)
        ret = []
        for key in charSet2List:
            if len(charSet2List[key]) >= 2:
                ret.extend(charSet2List[key])
        return ret