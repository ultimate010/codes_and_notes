/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/count-1-in-binary
@Language: C++
@Datetime: 16-08-04 01:59
*/

class Solution {
public:
    /**
     * @param num: an integer
     * @return: an integer, the number of ones in num
     */
    int countOnes(int num) {
        // write your code here
        int count = 0;
        while (num) {
            count++;
            num = num & (num - 1);
        }
        return count;
    }
};