# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/data-stream-median
@Language: Python
@Datetime: 16-06-15 06:10
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        # write your code here
        import heapq
        self.minHeap = []
        self.maxHeap = []
        self.curNum = 0
        def addHeap(num):
            # print self.maxHeap, self.minHeap
            
            if self.curNum % 2 == 0:  # even
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
            self.curNum += 1
            if len(self.maxHeap) == 0 or len(self.minHeap) == 0:
                return
            
            if -self.maxHeap[0] > self.minHeap[0]:
                maxV = -self.maxHeap[0]
                minV = self.minHeap[0]
                heapq.heapreplace(self.maxHeap, -minV)
                heapq.heapreplace(self.minHeap, maxV)
        ret = []
        for num in nums:
            addHeap(num)
            ret.append(-self.maxHeap[0])
        return ret