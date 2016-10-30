/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/print-numbers-by-recursion
@Language: C++
@Datetime: 16-06-15 13:54
*/

class Solution {
public:
    /**
     * @param n: An integer.
     * return : An array storing 1 to the largest number with n digits.
     */
    vector<int> numbersByRecursion(int n) {
        // write your code here
        vector<int> ret;
        if (n == 0)
            return ret;
        int i;
        vector<int> tmp = numbersByRecursion(n - 1);
        for (int i = 0; i< tmp.size();i++) 
            ret.push_back(tmp[i]);
        for (i = int(pow(10, n - 1)); i < int(pow(10,n)); i++)
            ret.push_back(i);
        return ret;
    }
};