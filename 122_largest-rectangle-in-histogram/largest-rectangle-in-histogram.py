# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/largest-rectangle-in-histogram
@Language: Python
@Datetime: 16-06-14 15:31
'''

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
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
        
    def largestRectangleArea2(self, height):
        n = len(height)
        if n == 0:
            return 0
        res = 0
        for i in range(n):
            if i + 1 < n and height[i] < height[i + 1]:  # i is heigher
                continue
            minH = height[i]
            for j in range(i, -1, -1):
                minH = min(minH, height[j])
                res = max(res, minH * (i - j + 1))
        return res
                
        
    def largestRectangleArea1(self, height):
        # write your code here
        n = len(height)
        if n == 0:
            return 0
        if n == 1:
            return height[0]
        maxCount = 0
        for i in range(n - 1):
            for j in range(i + 1, n + 1):
                count = (j - i) * min(height[i:j])
                # print height[i:j], j, i
                maxCount = count if count > maxCount else maxCount
        return maxCount