/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/search-a-2d-matrix-ii
@Language: C++
@Datetime: 16-06-15 12:55
*/

class Solution {
public:
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     */
    int searchMatrix(vector<vector<int> > &matrix, int target) {
        // write your code here
        int m = matrix.size();
        if (m == 0) 
            return 0;
        int n = matrix[0].size();
        int row = m - 1;
        int col = 0; 
        int count = 0;
        while (row >= 0 and col < n) {
            if (matrix[row][col] == target) {
                count += 1;
                row -= 1;
                col += 1;
            } else if (matrix[row][col] > target)
                row -= 1;
            else
                col += 1;
        }
        return count;
    }
};
