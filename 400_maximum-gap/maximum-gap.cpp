/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-gap
@Language: C++
@Datetime: 16-07-03 13:52
*/

class Solution {
public:
    /**
     * @param nums: a vector of integers
     * @return: the maximum difference
     */
    int maximumGap(vector<int> nums) {
        // write your code here
        int len = nums.size();
        if (len < 2)
            return 0;
        sort(nums.begin(), nums.end());
        int ret = 0;
        for (int i = 0;i <  len - 1; i++) {
            int t = nums[i + 1] - nums[i];
            if (t > ret)
                ret = t;
        }
        return ret;
    }
};