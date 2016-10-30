# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/first-bad-version
@Language: Python
@Datetime: 16-06-08 01:11
'''

#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        begin = 1
        end = n
        while begin < end:
            middle = (begin + end) / 2
            if not SVNRepo.isBadVersion(middle):
                # true, find in the right
                begin = middle + 1
            else:
                # false, find in the left
                end = middle
        return begin