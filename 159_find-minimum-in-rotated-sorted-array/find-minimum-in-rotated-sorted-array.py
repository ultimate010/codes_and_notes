# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array
@Language: Python
@Datetime: 16-06-27 15:28
'''

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        l, r = 0, len(num) - 1
        if not num:
            return 0
        while l < r:
            mid = (l + r) / 2
            if num[mid] < num[r]:
                r = mid
            elif num[mid] > num[r]:
                l = mid + 1
        return num[l]