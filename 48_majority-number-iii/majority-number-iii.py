# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/majority-number-iii
@Language: Python
@Datetime: 16-06-09 10:19
'''

class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        return self.method(nums, k)
            
    def subMethod(self, hash):
        for n in hash:
            if hash[n] == 0:
                return n
        return None
                
    def method(self, nums, k):
        hash = {}
    
        for i in range(-(k - 1), 0):
            hash[i] = 0
        for num in nums:
           
            if num in hash:
                hash[num] += 1
            else:
                n = self.subMethod(hash)        
                if n is not None:
                    del hash[n]
                    hash[num] = 1
                else:
                    for n in hash:
                        hash[n] -= 1
        for key in hash:
            hash[key] = 0
        for num in nums:
            if num in hash:
                hash[num] += 1
        # print hash
        for key in hash:
            if hash[key] > len(nums) / k:
                return key