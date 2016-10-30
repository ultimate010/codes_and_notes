# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/super-ugly-number
@Language: Python
@Datetime: 16-06-30 15:29
'''

class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        # Write your code here
        import heapq
        uglys = [1]
        prims = primes
        times = [0] * len(prims)
        heap = [[prims[i], i] for i in range(len(prims))]
        heapq.heapify(heap)
        while len(uglys) < n:
            num, choose = heapq.heappop(heap)
            if num != uglys[-1]:
                uglys.append(num)
            times[choose] += 1
            heapq.heappush(heap, [prims[choose] * uglys[times[choose]], choose])
        # print uglys
        return uglys[-1]