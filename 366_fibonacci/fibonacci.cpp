/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/fibonacci
@Language: C++
@Datetime: 16-08-03 15:47
*/

class Solution{
public:
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    int fibonacci(int n) {
        // write your code here
        if (n == 1) 
            return 0;
        if (n == 2)
            return 1;
        int pprev = 0, prev = 1;
        int tmp;
        while (--n > 2)
        {
            tmp = prev;
            prev = pprev + prev;
            pprev = tmp;
        }
        return prev + pprev;
    }
};
