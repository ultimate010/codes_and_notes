# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/triangle
@Language: Python
@Datetime: 16-06-13 03:09
'''

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        
        rows = len(triangle)
        for row in range(rows - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], 
                triangle[row+1][col+1])
        return triangle[0][0]