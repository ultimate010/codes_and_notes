# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/restore-ip-addresses
@Language: Python
@Datetime: 16-06-30 12:06
'''

class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        # Write your code here
        ret = []
        def dfs(s, n, i, seg, path, tmp):
            if tmp and int(tmp) > 255 or (len(tmp) > 1 and tmp[0] == '0'):
                return
            # print seg, '#', path, '#', tmp
            
            if seg == 3 and i == n:
                ret.append(path + '.' + tmp)
            if i == n:
                return 
            #seg
            if path:
                
                dfs(s, n, i + 1, seg + 1, path + '.' + tmp, s[i])
            else:
                if tmp:
                    
                    dfs(s, n, i + 1, seg + 1, tmp, s[i])
                
            #not seg
            dfs(s, n, i + 1, seg, path, tmp + s[i])
            
        dfs(s, len(s), 0, 0, '', '')
        
        return ret