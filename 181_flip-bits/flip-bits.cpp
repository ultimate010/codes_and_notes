/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/flip-bits
@Language: C++
@Datetime: 16-06-08 04:17
*/

class Solution {
public:
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    int bitSwapRequired(int a, int b) {
        // write your code here
        int c = a ^ b;
        int count = 0;
        while (c != 0){
            // count += c & 0x01;
            count += 1;
            c = c & (c - 1);
        }
        return count;
    }
};