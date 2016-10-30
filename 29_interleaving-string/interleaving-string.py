# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/interleaving-string
@Language: Python
@Datetime: 16-06-14 05:35
'''

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave1(self, s1, s2, s3):
        # write your code here
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s1) + len(s2) != len(s3):
            return False

        interleave = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        interleave[0][0] = True
        for i in range(len(s1)):
            interleave[i + 1][0] = s1[:i + 1] == s3[:i + 1]
        for i in range(len(s2)):
            interleave[0][i + 1] = s2[:i + 1] == s3[:i + 1]

        for i in range(len(s1)):
            for j in range(len(s2)):
                interleave[i + 1][j + 1] = False
                if s1[i] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] = interleave[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] |= interleave[i + 1][j]
        return interleave[len(s1)][len(s2)]
        
    def isInterleave(self, s1, s2, s3):
        # write your code here
        nS1 = len(s1)
        nS2 = len(s2)
        nS3 = len(s3)
        if nS1 + nS2 != nS3:
            return False
        matrix = [[True for j in range(nS2 + 1)] for i in range(nS1 + 1)]
        for i in range(1, nS1 + 1):
            matrix[i][0] = s1[:i] == s3[:i]
        for i in range(1, nS2 + 1):
            matrix[0][i] = s2[:i] == s3[:i]
        for i in range(nS1):
            for j in range(nS2):
                matrix[i + 1][j + 1] = False
                if s1[i] == s3[i + j + 1]:
                    matrix[i + 1][j + 1] = matrix[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    # use or instead of and
                    matrix[i + 1][j + 1] |= matrix[i + 1][j]  
        return matrix[-1][-1]