# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/singleton
@Language: Python
@Datetime: 16-06-15 06:25
'''

class Solution:
    # @return: The same instance of this class every time
    curInstance = None
    @classmethod
    def getInstance(cls):
        # write your code here
        if cls.curInstance is None:
            cls.curInstance = Solution()
        return cls.curInstance