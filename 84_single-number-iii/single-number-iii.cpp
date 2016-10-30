/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/single-number-iii
@Language: C++
@Datetime: 16-06-09 08:29
*/

class Solution {
public:
    /**
     * @param A : An integer array
     * @return : Two integers
     */
    vector<int> singleNumberIII(vector<int> &A) {
        // write your code here
        int c = 0;
        for (int i = 0; i < A.size(); i++) {
            c ^= A[i];
        }
        int pos = 0;
        for ( pos = 0; pos < 32; pos++ ) {
            if (c >> pos & 1) {
                break;
            }
        }
        vector<int> a,b;
        for (int i = 0; i < A.size(); i++) {
            if (A[i] >> pos & 1) {
                a.push_back(A[i]);
            } else {
                b.push_back(A[i]);
            }
        }
        
        vector<int> res;
        res.push_back(0);
        res.push_back(0);
        
        for (int i = 0; i < a.size(); i++) {
            res[0] ^= a[i];
        }
        for (int i = 0; i < b.size(); i++) {
            res[1] ^= b[i];
        }
        return res;
    }
};