# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/backpack
@Language: Python
@Datetime: 16-06-13 14:28
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [0 for x in range(m+1)]
        dp[0] = 1  # can get i capacity 
        ans = 0
        for item in A:
            for i in range(m,-1,-1):
                if i-item >=0 and dp[i-item] > 0:
                    ans = max(ans,i)
                    dp[i] = 1
        return ans    
        
    def backPack12(self, m, A):
        f = [0 for i in range(m + 1)]
        for i in xrange(1, len(A) + 1):
            for j in xrange(m, 0 , -1):
                if j - A[i - 1] >= 0:
                    f[j] = max(f[j], f[j - A[i - 1]] + A[i -1])
                
        return f[-1]    
        
    def mybackPack(self, m, A):
        f = [[0 for i in range(m + 1)], [0 for i in range(m + 1)]]
        prev, cur = 0, 1
        for i in xrange(1, len(A) + 1):
            prev, cur = cur, prev
            for j in xrange(1, m + 1):
                if j - A[i - 1] >= 0:  # there is space for this package
                    f[cur][j] = max(f[prev][j], f[prev][j - A[i- 1]] + A[i-1])
                else:  # can not put this package into backpack
                    f[cur][j] = f[prev][j]
        # print f[cur]
        return f[cur][-1]

                
    
    def backPack1(self, m, A):
        # write your code here
        
        def dfs(m, A, path, start):
            count = 0
            for n in path:
                count += n
            if count > m:
                return
            if start == len(A):  # to the end
                global maxSize
                if maxSize < count:
                    maxSize = count
            else:
                path.append(A[start])  # chose this 
                dfs(m, A, path, start + 1)
                path.pop()
                dfs(m, A, path, start + 1)
        global maxSize
        maxSize = 0                
        dfs(m, A, [], 0)
        
        return maxSize