/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-common-substring
@Language: C++
@Datetime: 16-07-04 08:29
*/

class Solution {
public:    
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    int longestCommonSubstring(string &A, string &B) {
        // write your code here
        int m = A.size();
        int n = B.size();
        if (m == 0 || n == 0) 
            return 0;
        vector< vector<int> > dp(m + 1, vector<int>(n + 1, 0));
        int ret  = 0;
        for(int row = 1;row <= m; row++) {
            for (int col = 1; col <= n; col++) {
                if (A[row - 1] == B[col - 1]) {
                    dp[row][col] = dp[row - 1][col - 1] + 1;
                    ret = max(ret, dp[row][col]);
                }
            }
        }
        return ret;
    }
};
