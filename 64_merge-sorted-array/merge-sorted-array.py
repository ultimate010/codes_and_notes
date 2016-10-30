# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/merge-sorted-array
@Language: Python
@Datetime: 16-06-07 05:17
'''

class Solution:
    def shiftAndInsert(self, A, m, insertPos, num):
        for pos in range(m - 1, insertPos, -1):
            A[pos] = A[pos - 1]
        A[insertPos] = num
            
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if n < 0 or m < 0:
            return 
        return self.method2(A, m, B, n)
    def method2(self, A, m, B, n):
        insertPosRec = []
        aPos = 0
        for pos in range(n):
            while aPos < m and A[aPos] < B[pos]:
                aPos += 1
            insertPosRec.append(aPos)
        lastRangeRight = m + n - 1
        for pos in range(n - 1, -1 , -1):
            num = B[pos]
            insertPos = insertPosRec[pos]
            shiftLen = pos + 1
            for j in range(lastRangeRight, insertPos + shiftLen - 1, -1):
                A[j] = A[j - shiftLen]
            A[insertPos + pos] = num
            lastRangeRight = insertPos + pos - 1
                
    def method1(self, A, m, B, n):
        aPos = 0
        for i in range(n):
            while aPos < m + n and A[aPos] != 0 and A[aPos] < B[i]:
                aPos += 1
            # insert b into A
            self.shiftAndInsert(A, m + n, aPos, B[i])
            aPos += 1
            
            