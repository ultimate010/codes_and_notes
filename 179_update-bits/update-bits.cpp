/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/update-bits
@Language: C++
@Datetime: 16-06-08 06:25
*/

class Solution {
public:
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    int updateBits(int n, int m, int i, int j) {
        // write your code here
        int mask1 = 0x80000000;
        int mask2 = 0xffffffff;
        int mask = 0;
        m = m << i;
        if (j == 31)
        {
            mask = mask2 << i;
        } else {
            mask = (mask1 >> ( 30 - j)) ^ (mask2 << i);
        }
        return n & (~mask) | m ;
    }
};