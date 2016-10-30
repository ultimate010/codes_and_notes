# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-serialization
@Language: Python
@Datetime: 16-06-12 05:36
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        ret = []
        self.serializeHelper(root, ret)
        # print ret
        return ret
        
    def serializeHelper(self, root, ret):
        if root is None:
            ret.append('#')
        else:
            ret.append(root.val)
            self.serializeHelper(root.left, ret)
            self.serializeHelper(root.right, ret)
            
    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        self.pos = 0
        return self.deserializeHelper(data)
    
    def deserializeHelper(self, data):
        if self.pos == len(data):
            return None
        if data[self.pos] == '#':
            return None
        else:
            # print data[self.pos], data[self.pos+1], data[self.pos+2]
            root = TreeNode(data[self.pos])
            self.pos += 1
            root.left = self.deserializeHelper(data)
            self.pos += 1
            root.right = self.deserializeHelper(data)
            return root