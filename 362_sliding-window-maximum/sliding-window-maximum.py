# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/sliding-window-maximum
@Language: Python
@Datetime: 16-06-16 10:27
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        from collections import deque
        queue = deque()
        n = len(nums)
        if n == 0:
            return []
        pos = 0
        ret = []
        count = k
        while pos < n and count > 0:
            while len(queue) > 0 and queue[-1] < nums[pos]:  # remove small num
                queue.pop()
            queue.append(nums[pos])
            count -= 1
            pos += 1
        for i in range(k - 1, n):
            if nums[i-k] == queue[0]:
                queue.popleft()  # pop left
            while len(queue) > 0 and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
            ret.append(queue[0])
            i += 1
            # print queue
        
        return ret