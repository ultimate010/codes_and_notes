/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/space-replacement
@Language: C++
@Datetime: 16-08-04 01:38
*/

class Solution {
public:
    /**
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    int replaceBlank(char string[], int length) {
        // Write your code here
        int spaceCount = 0;
        
        for (int i = 0; i < length; i++)
            if (string[i] == ' ')
                spaceCount++;
        int ret = length + spaceCount * 2;        
        for (int i = length - 1;i >= 0; i--){
            if (string[i] == ' '){
                spaceCount--;
                strncpy(string + i + spaceCount * 2, "%20", 3);
            } else {
                string[i + spaceCount * 2] = string[i];
            }
        }
        return ret;
    }
};  