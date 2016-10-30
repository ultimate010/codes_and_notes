/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/string-to-integer-ii
@Language: C++
@Datetime: 16-06-16 05:50
*/

class Solution {
public:
    /**
     * @param str: A string
     * @return An integer
     */
    int atoi(string str) {
        // write your code here
        if (str.size() == 0)
            return 0;
        bool flag = false;
        int pos = 0;
        long num = 0;
        while (pos < str.size() && str[pos] == ' ')
            pos += 1;
        if (pos == str.size())  // to the end
            return 0;
        if (str[pos] == '-') {
            pos += 1;
            flag = true;
        } else if (str[pos] == '+') {
            pos += 1;
            flag = false;
        }
        
        
        bool begin = true;
        
        while (pos < str.size())
        {
            // cout << pos << " " << str[pos] << endl;
            if (begin && str[pos] == '0') {  // illegal like '[-]0xxxx'
                pos += 1;
                continue;
            }
                
            begin = false;
            if (str[pos] <= '9' && str[pos] >= '0') { // legal number
                 num *= 10;
                 num += str[pos] - '0';
                 pos += 1;
                 if (num > INT_MAX) {
                    return flag ? -2147483648: 2147483647;
                 }
            } else if (str[pos] == '.')  // end of integer like 3.23
                break;
            else
                // illegal number
                break;
        }
        if (flag)
            return -num;
        return num;
    }
};