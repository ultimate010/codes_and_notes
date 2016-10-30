/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/single-number-ii
@Language: C++
@Datetime: 16-06-09 08:23
*/

class Solution {
public:
	/**
	 * @param A : An integer array
	 * @return : An integer 
	 */
    int singleNumberII(vector<int> &A) {
        // write your code here
        int result = 0;
        for (int i = 0;i < 32; i++) {
            int count = 0;
            for (int j = 0;j < A.size(); j++) {
                int t = A[j] >> i;
                count += t & 1;
            }
            result += (count % 3) << i;
        }
        return result;
    }
};