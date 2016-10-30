# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/kth-largest-element
@Language: Python
@Datetime: 16-06-16 04:47
'''

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        import heapq
        if len(A) == 0:
            return None
        heap = []
        for n in A:
            if len(heap) < k:
                heapq.heappush(heap, n)
                continue
            if heap[0] < n:
                heapq.heapreplace(heap, n)
        return heap[0]