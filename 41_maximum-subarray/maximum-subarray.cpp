/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-subarray
@Language: C++
@Datetime: 16-07-04 15:48
*/

class Solution {
public:    
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    int maxSubArray(vector<int> nums) {
        // write your code here
        if (nums.size() == 0)
            return 0;
        int curSum = 0;
        int ret = nums[0];
        for (auto n : nums) {
            curSum = max(n, curSum + n);
            ret = max(ret, curSum);
        }
        return ret;
    }
};
