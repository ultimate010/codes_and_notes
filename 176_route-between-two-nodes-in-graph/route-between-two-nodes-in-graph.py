# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/route-between-two-nodes-in-graph
@Language: Python
@Datetime: 16-06-28 07:32
'''

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        from collections import deque
        visited = {}
        queue = deque()
        queue.append(s)
        while queue:
            p = queue.popleft()
            if p in visited:
                continue
            visited[p] = True
            if p == t:
                return True
            for i in p.neighbors:
                queue.append(i)
        return False
        
    def hasRoute1(self, graph, s, t):
        # write your code here
        def dfs(s, t):
            if s == t:
                return True
            for n in s.neighbors:
                if dfs(n, t):
                    return True
            return False
        return dfs(s, t)