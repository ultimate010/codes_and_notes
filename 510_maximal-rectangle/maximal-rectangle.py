# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximal-rectangle
@Language: Python
@Datetime: 16-07-08 09:26
'''

class Solution:
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    def maximalRectangle(self, matrix):
        # Write your code here
        m = len(matrix)  
        if m == 0: return 0
        n = len(matrix[0])
        ret = 0
        height = [0] * n 
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    height[col] = 0
                else:
                    height[col] += 1
            ret = max(ret, self.largestRectangleArea(height))
        return ret
            
    def largestRectangleArea(self, height):
        # write your code here
        stack=[]; i=0; area=0
        while i<len(height):
            if stack==[] or height[i]>height[stack[len(stack)-1]]:
                stack.append(i)
            else:
                curr=stack.pop()
                width=i if stack==[] else i-stack[len(stack)-1]-1
                area=max(area,width*height[curr])
                i-=1
            i+=1
        while stack!=[]:
            curr=stack.pop()
            width=i if stack==[] else len(height)-stack[len(stack)-1]-1
            area=max(area,width*height[curr])
        return area