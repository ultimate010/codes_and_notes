# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/search-in-rotated-sorted-array
@Language: Python
@Datetime: 16-06-23 02:36
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        low, high = 0, len(A) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if target == A[mid]:
                return mid
            elif (A[mid] > A[low] and A[mid] > target and target >= A[low]) or \
            (A[mid] < A[low] and not (target <= A[high] and target > A[mid])):
                high = mid - 1
            else:
                low = mid + 1
        return -1
            
            
    def search1(self, A, target):
        # write your code here
        if len(A) == 0:
            return -1
        if A[0] > target:
            end = len(A) - 1
            while end > 0:
                if A[end] == target:
                    return end
                end -= 1
        else:
            begin = 0
            while begin < len(A):
                if A[begin] == target:
                    return begin
                begin += 1
        return -1