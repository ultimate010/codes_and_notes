/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/burst-balloons
@Language: C++
@Datetime: 16-07-03 13:42
*/

class Solution {
public:
    /**
     * @param nums a list of integer
     * @return an integer, maximum coins
     */  
    int helper(vector< vector<int> > & dp, vector<int> & nums, int start, int end) {
        if (dp[start][end] != 0)
            return dp[start][end];
        for (int i = start; i <= end; i++) {
            int t = helper(dp, nums, start, i - 1) + nums[start - 1] * nums[i] * nums[end + 1] + helper(dp, nums, i + 1, end);
            if (t > dp[start][end]) 
                dp[start][end] = t;
        }
        return dp[start][end];
    }
    int maxCoins(vector<int>& nums) {
        // Write your code here
        int len = nums.size();
        nums.insert(nums.begin(), 1);
        nums.insert(nums.end(), 1);
        vector< vector<int> > dp(len + 2, vector<int>(len + 2, 0));
        return helper(dp, nums, 1, len);
    }
};
