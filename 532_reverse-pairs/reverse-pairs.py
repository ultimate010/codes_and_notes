# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/reverse-pairs
@Language: Python
@Datetime: 16-06-16 02:29
'''

class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    def reversePairs(self, A):
        #  merge sort 
        global count
        count = 0
        def mergeSort(A, start, end):
            if start >= end - 1:  # only one node
                return 
            mid = start + (end - start) / 2
            mergeSort(A, start, mid)  # left close right open
            mergeSort(A, mid, end)
            merge(A, start, mid, end)
            
        def merge(A, start, mid, end):
            p1 = start
            p2 = mid
            tmp = []
            global count 
            while p1 < mid  and p2 < end:
                if A[p1] <= A[p2]:
                    tmp.append(A[p1])
                    p1 += 1
                else:
                    tmp.append(A[p2])
                    p2 += 1
                    count += mid - p1
                    # because the right is bigger like [3, 4, 1, 2] [1, 2, 3, 4]
            while p1 < mid:
                tmp.append(A[p1])
                p1 += 1
            while p2 < end:
                tmp.append(A[p2])
                p2 += 1
            # print A, tmp, count
            A[start:end] = tmp
                    
        mergeSort(A, 0, len(A))
        return count
        
    def reversePairs1(self, A):
        # Write your code here
        if len(A) <= 1:
            return 0
        count = 0
        for i in range(1, len(A)):
            for j in range(i):
                if A[j] > A[i]:
                    count += 1
        return count