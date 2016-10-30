# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/clone-graph
@Language: Python
@Datetime: 16-06-24 10:33
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None
        if node.label in self.dict:
            return self.dict[node.label]
        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root
        for n in node.neighbors:
            root.neighbors.append(self.cloneGraph(n))
        return root