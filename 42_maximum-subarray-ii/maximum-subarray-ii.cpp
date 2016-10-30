/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-subarray-ii
@Language: C++
@Datetime: 16-07-05 07:58
*/

class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    int maxTwoSubArrays(vector<int> nums) {
        // write your code here
        int n = nums.size();
        vector<int> dp1(n + 1, INT_MIN);
        vector<int> dp11(n + 1, INT_MIN);
        vector<int> dp2(n + 1, INT_MIN);
        vector<int> dp22(n + 1, INT_MIN);
        dp1[0] = dp2[n] = 0;
        for (int i = 1; i <= n; i++) {
            dp1[i] = max(dp1[i - 1] + nums[i - 1], nums[i - 1]);
            dp11[i] = max(dp11[i - 1], dp1[i]);
        }
        for (int i = n; i >= 1; i--) {
            dp2[i - 1] = max(dp2[i] + nums[i - 1], nums[i - 1]);
            dp22[i - 1] = max(dp22[i], dp2[i - 1]);
        }
        int ret = INT_MIN;
        for (int i = 1; i < n; i++) {
            // cout << dp11[i] << dp22[i] << endl;
            ret = max(ret, dp11[i] + dp22[i]);
        }
        return ret;
    }
};
