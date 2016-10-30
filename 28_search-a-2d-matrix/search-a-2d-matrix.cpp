/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/search-a-2d-matrix
@Language: C++
@Datetime: 16-06-15 12:45
*/

class Solution {
public:
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        // write your code here
        int row = 0;
        int col = 0;
        int m = matrix.size();
        if (m == 0 || matrix[0].size() == 0) 
            return false;
        int n = matrix[0].size();
        for (; row < m; row++) {
            if (matrix[row][n - 1] > target) {
                break;
            } else if (matrix[row][n - 1] == target) {
                return true;  
            }
        }
        if (row == m)
            return false;
        
        for (; col < n; col++) {
            if (matrix[row][col] == target) 
                return true;
        }
        return false;
    }
};
