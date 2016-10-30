/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/continuous-subarray-sum
@Language: C++
@Datetime: 16-07-04 15:57
*/

class Solution {
public:
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of 
     *          the first number and the index of the last number
     */
    vector<int> continuousSubarraySum(vector<int>& A) {
        // Write your code here
        if (A.size() == 0)
            return vector<int>(2, 0);
        vector<int> ret(2, 0);
        int curSum = 0;
        int maxSum = A[0];
        int prev = 0;
        int pos = 0;
        for (auto n: A) {
            if (curSum + n < n) {
                prev = pos;
                curSum = n;
            } else 
                curSum += n;
            if (maxSum < curSum) {
                maxSum = curSum;
                ret[0] = prev;
                ret[1] = pos;
            }

            ++pos;
        }
        return ret;
    }
};