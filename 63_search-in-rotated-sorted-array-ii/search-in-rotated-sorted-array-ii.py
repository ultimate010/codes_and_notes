# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/search-in-rotated-sorted-array-ii
@Language: Python
@Datetime: 16-06-23 02:58
'''

class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        for i in A:
            if i == target:
                return True
        return False