/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/interleaving-string
@Language: C++
@Datetime: 16-07-04 15:41
*/

class Solution {
public:
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true of false.
     */
    bool isInterleave(string s1, string s2, string s3) {
        // write your code here
        int m = s1.size();
        int n = s2.size();
        if (m + n != s3.size())
            return false;
        vector< vector<bool> > dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;
        for (int i = 1; i <= m; i++) {
            if (s1[i - 1] == s3[i - 1])
                dp[i][0] = dp[i - 1][0];
        }
        for (int i = 1; i <= n; i++) {
            if (s2[i - 1] == s3[i - 1])
                dp[0][i] = dp[0][i - 1];
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s3[i + j - 1]) 
                    dp[i][j] = dp[i - 1][j];
                if (s2[j - 1] == s3[i + j - 1]) 
                    dp[i][j] = dp[i][j - 1] == true? true: dp[i][j];
            }
        }
        return dp[m][n];
    }
};