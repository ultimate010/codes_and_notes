/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/minimum-adjustment-cost
@Language: C++
@Datetime: 16-07-04 15:04
*/

class Solution {
public:
    /**
     * @param A: An integer array.
     * @param target: An integer.
     */
    int MinAdjustmentCost(vector<int> A, int target) {
        // write your code here
        int m = A.size();
        vector< vector<int> > matrix(m + 1, vector<int>(101, INT_MAX));
        for (int i = 0; i <= 100; i++) 
            matrix[0][i] = 0;
        for (int i = 1;i <= m; i++ ) {
            for (int j = 1;j <= 100; j++ ) {
                for (int k = 0;k <= target; k++) {
                    if ( j - k > 0 ) {
                        matrix[i][j] = min(matrix[i][j], matrix[i - 1][j - k] + abs(A[i - 1] - j));
                    } 
                    if ( j + k <= 100 ) {
                        matrix[i][j] = min(matrix[i][j], matrix[i - 1][j + k] + abs(A[i - 1] - j));
                    } 
                }
            }
        }
        int ret = INT_MAX;
        for (int i = 1; i <= 100; i++) {
            if (ret > matrix[m][i])
                ret = matrix[m][i];
        }
        return ret;
    }
};