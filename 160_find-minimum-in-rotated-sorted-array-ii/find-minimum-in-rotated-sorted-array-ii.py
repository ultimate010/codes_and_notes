# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array-ii
@Language: Python
@Datetime: 16-06-27 15:23
'''

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        low, high = 0, len(num) - 1
        while low < high:
            mid = low + (high - low) / 2
            if num[mid] < num[high]:
                high = mid
            elif num[mid] > num[high]:
                low = mid + 1
            else:
                high = high - 1
        return num[low]