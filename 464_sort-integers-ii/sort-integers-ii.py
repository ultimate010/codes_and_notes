# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/sort-integers-ii
@Language: Python
@Datetime: 16-06-19 11:23
'''

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        heap = []
        import heapq
        for i in A:
            heapq.heappush(heap, i)
        for i in range(len(A)):
            A[i] = heapq.heappop(heap)
            
            
    def sortIntegers3(self, A):
        # merge sort
        def mergeSort(A):
            if len(A) <= 1:
                return A
            mid = len(A) / 2
            l = mergeSort(A[:mid])
            r = mergeSort(A[mid:])
            return merge(l, r)
            
        def merge(A, B):
            ret = []
            i, j = 0, 0
            while i < len(A) and j < len(B):
                if A[i] <= B[j]:
                    ret.append(A[i])
                    i += 1
                else:
                    ret.append(B[j])
                    j += 1
            while i < len(A):
                ret.append(A[i])
                i += 1
            while j < len(B):
                ret.append(B[j])
                j += 1
            return ret
                
        ret = mergeSort(A)
        for pos, i in enumerate(ret):
            A[pos] = i
        
            
    def sortIntegers1(self, A):
        # Write your code here
        def partition1(A, start, end):
            if start >= end:
                return start
            i, j = start, start + 1
            while j < end:
                if A[j] >= A[start]:
                    pass
                else:
                    A[i + 1], A[j] = A[j], A[i + 1]
                    i += 1
                j += 1
            A[start], A[i] = A[i], A[start]
            return i
            
        def partition(A, start, end):
            if start >= end:
                return start
            tmp = A[start]
            while start < end:
                while end > start and A[end] >= tmp:
                    end -= 1
                A[start], A[end] = A[end], A[start]
                while start < end and A[start] <= tmp:
                    start += 1
                A[start], A[end] = A[end], A[start]
            A[start] = tmp
            
            return start
            
            
        def qsort(A, start, end):
            if start < end:
                mid = partition1(A, start, end)
                qsort(A, start , mid - 1)
                qsort(A, mid + 1, end)
                
        start, end = 0, len(A) - 1
        return qsort(A, start, end)