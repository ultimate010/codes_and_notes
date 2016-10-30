/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/find-the-missing-number
@Language: C++
@Datetime: 16-06-28 05:14
*/

class Solution {
public:
    /**    
     * @param nums: a vector of integers
     * @return: an integer
     */
    int findMissing(vector<int> &nums) {
        int i = 0 , n = nums.size();
        while (i < n)
        {
            while (nums[i] != i && nums[i] < n)
                swap(nums[i], nums[nums[i]]);
            ++i;
        }
        for(int i = 0; i < n; i++)
            if (nums[i] != i)
                return i;
        return n;
    }
    int findMissing1(vector<int> &nums) {
        // write your code here
        int count = 0;
        sort(nums.begin(), nums.end());
        for (auto i:nums) {
            if (i != count)
                return count;
            count++;
        }
        return count;
    }
};