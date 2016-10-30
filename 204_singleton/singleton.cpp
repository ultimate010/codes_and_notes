/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/singleton
@Language: C++
@Datetime: 16-08-03 15:51
*/

class Solution {
public:
    /**
     * @return: The same instance of this class every time
     */
    static Solution* getInstance() {
        // write your code here
        static Solution * point = NULL;
        if (point == NULL)
            point = new Solution();
        return point;
    }
};