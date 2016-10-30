# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/topological-sorting
@Language: Python
@Datetime: 16-06-12 09:03
'''

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import defaultdict
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        if len(graph) == 0:
            return []
        inMap = defaultdict(int)
        for node in graph:
            if node not in inMap:
                inMap[node] = 0
            for neb in node.neighbors:
                # print node.label, '-', neb.label
                inMap[neb] += 1

        ret = []        
        stack = []
        # print inMap
        for node in inMap:
            if inMap[node] == 0:
                # print '#', node.label
                stack.append(node)

        while len(stack) > 0:
            node = stack.pop()
            # print node.label
            ret.append(node)
            for neb in node.neighbors:
                inMap[neb] -= 1
                if inMap[neb] == 0:
                    stack.append(neb)
            inMap[node] = -1  # remove cur node
                    
        return ret