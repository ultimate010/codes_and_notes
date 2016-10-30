/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array
@Language: C++
@Datetime: 16-08-05 08:14
*/

class Solution {
public:
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
    int findMin(vector<int> &num) {
        // write your code here
        int left = 0, right = num.size() - 1;
        int mid;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (num[mid] < num[right])
                right = mid;
            else
                left = mid + 1;
        }
        return num[left];
    }
};