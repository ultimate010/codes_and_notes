# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/ugly-number-ii
@Language: Python
@Datetime: 16-06-14 11:49
'''

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        import heapq
        uglys = [1]
        prims = [2, 3, 5]
        times = [0] * 3
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
        
    def nthUglyNumber1(self, n):
        # write your code here
        times = [0] * 3
        uglys = [float('inf')] * n
        prims = [2, 3, 5]
        uglys[0] = 1
        for i in range(1, n):
        
            for j in range(3):
                uglys[i] = min(uglys[i], uglys[times[j]] * prims[j])
        
            for j in range(3):
        
                if uglys[i] == uglys[times[j]] * prims[j]:
                    times[j] += 1
        
        
        return uglys[-1]