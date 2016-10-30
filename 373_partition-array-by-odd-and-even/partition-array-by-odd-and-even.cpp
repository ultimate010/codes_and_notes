/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/partition-array-by-odd-and-even
@Language: C++
@Datetime: 16-06-15 13:30
*/

class Solution {
public:
    /**
     * @param nums: a vector of integers
     * @return: nothing
     */
    void partitionArray(vector<int> &nums) {
        int length = nums.size();
        if (length == 0) 
            return ;
        int prev = 0, next = 1, tmp;
        while (next < length) {
            if (nums[next] % 2 != 0) {  // odd put to the left
                tmp = nums[prev + 1];
                nums[prev + 1] = nums[next];
                nums[next] = tmp;
                prev++;
            }
            next++;
        }
        tmp = nums[prev];
        nums[prev] = nums[0];
        nums[0] = tmp;
        return ;
    }
    void partitionArray1(vector<int> &nums) {
        // write your code here
        int length = nums.size();
        if (length == 0) 
            return ;
        int i = 0, j = length - 1;
        int tmp = nums[0];
        while (i < j) {
            while (nums[j] % 2 == 0 && j > i)
                j--;
            nums[i] = nums[j]; 
            while (nums[i] % 2 != 0 && j > i) 
                i++;
            nums[j] = nums[i]; 
        }
        nums[i] = tmp;
        return ;
    }
};