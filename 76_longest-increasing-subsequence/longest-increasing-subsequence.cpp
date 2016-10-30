/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-increasing-subsequence
@Language: C++
@Datetime: 16-07-04 08:53
*/

class Solution {
public:
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    int longestIncreasingSubsequence(vector<int> nums) {
        // write your code here
        int n = nums.size();
        if (n == 0)
            return 0;
        vector<int> count(n, 1);
        int ret = 0;
        for (int i = 1;i < n;i++) {
            int maxL = 0;
            for (int j = 0; j < i;j ++) {
                if (nums[j] <= nums[i]) {
                    maxL = max(maxL, count[j]);
                }
            }
            count[i] = maxL + 1;
            ret = max(ret, count[i]);
        }
        return ret;
    }
};
