# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/house-robber-iii
@Language: Python
@Datetime: 16-07-01 06:37
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        sef.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root, the root of binary tree.
    # @return {int} The maximum amount of money you can rob tonight
    def houseRobber3(self, root):
        def helper(root):
            if root is None:
                return 0, 0
            lr, ln = helper(root.left)
            rr, rn = helper(root.right)
            
            rb = root.val + ln + rn
            nr = max(lr, ln) + max(rr, rn)
            return rb, nr
        t, k = helper(root)    
        return max(t, k)
        
    hash = {}
    def houseRobber31(self, root):
        # write your code here
        if root in Solution.hash:
            return Solution.hash[root]
        
        if root is None:
            Solution.hash[root] = 0
            return 0
        l = self.houseRobber3(root.left)
        r = self.houseRobber3(root.right)
        ll, rr = 0, 0
        if root.left:
            ll = self.houseRobber3(root.left.left) + self.houseRobber3(root.left.right)
        if root.right:
            rr = self.houseRobber3(root.right.left) + self.houseRobber3(root.right.right)
        Solution.hash[root] = max(root.val + ll + rr, l + r)
        
        return Solution.hash[root]