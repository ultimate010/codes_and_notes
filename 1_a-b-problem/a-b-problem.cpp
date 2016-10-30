/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/a-b-problem
@Language: C++
@Datetime: 16-06-16 05:13
*/

class Solution {
public:
    /*
     * @param a: The first integer
     * @param b: The second integer
     * @return: The sum of a and b
     */
    int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        return (!b ? a : aplusb(a ^ b, (a & b) << 1));
    }
};