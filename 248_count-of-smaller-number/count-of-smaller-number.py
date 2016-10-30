# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/count-of-smaller-number
@Language: Python
@Datetime: 16-06-27 15:51
'''

class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        A = sorted(A)
        ret = []
        def helper(A, q):
            if not A:
                return 0
            l, r = 0, len(A) - 1
            while l < r:
                mid = (r + l) / 2
                if A[mid] == q:
                    l = mid
                    break
                elif A[mid] > q:
                    r = mid - 1
                else:
                    l = mid + 1 
            while l > 0 and A[l] == q:
                l -= 1
            if A[l] < q:
                return l + 1
            elif A[l] > q:
                return l
            else:
                return 0
            
        for q in queries:
            ret.append(helper(A, q))
        return ret