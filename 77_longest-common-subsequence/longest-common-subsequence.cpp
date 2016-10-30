/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-common-subsequence
@Language: C++
@Datetime: 16-07-04 08:36
*/

class Solution {
public:
    /**
     * @param A, B: Two strings.
     * @return: The length of longest common subsequence of A and B.
     */
    int longestCommonSubsequence(string A, string B) {
        // write your code here
        int m = A.size();
        int n = B.size();
        if (m == 0 || n == 0) {
            return 0;
        }
        vector< vector<int> > dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1;i <= m;i++) {
            for (int j = 1; j <= n; j++) {
                if (A[i - 1] == B[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = dp[i - 1][j] > dp[i][j]? dp[i - 1][j] : dp[i][j];
                    dp[i][j] = dp[i][j - 1] > dp[i][j]? dp[i][j - 1] : dp[i][j];
                }
            }
        }
        return dp[m][n];
    }
};
