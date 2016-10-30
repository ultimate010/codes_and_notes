/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/assignment-operator-overloading-c-only
@Language: C++
@Datetime: 16-06-28 05:01
*/

class Solution {
public:
    char *m_pData;
    Solution() {
        this->m_pData = NULL;
    }
    Solution(char *pData) {
        this->m_pData = pData;
    }

    // Implement an assignment operator
    Solution operator=(const Solution &object) {
        // write your code here
        if (this == &object) 
            return *this;
        if (this->m_pData) {
            delete [] this->m_pData;
            this->m_pData = NULL;
            
        }
        if (object.m_pData) {
            this->m_pData = new char[strlen(object.m_pData) + 1];
            strcpy(this->m_pData, object.m_pData);
        }
        return *this;
    }
};