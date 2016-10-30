/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/k-sum
@Language: C++
@Datetime: 16-06-18 08:21
*/

class Solution {
public:
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return an integer
     */
    int kSum(vector<int> A, int k, int target) {
        // wirte your code here
        int n = A.size();  
        vector<vector<int> > dp(k+1,vector<int>(target+1,0));  
        dp[0][0] = 1;  
        for(auto a:A)  
        {  
            for(int i=k;i>=1;i--)  
            {  
                for(int j=target;j>=a;j--)  
                {  
                    dp[i][j] += dp[i-1][j-a];  
                }  
            }  
        }  
        return dp[k][target];  
    }
};