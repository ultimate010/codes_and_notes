/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/implement-queue-by-two-stacks
@Language: C++
@Datetime: 16-08-05 13:35
*/

class Queue {
public:
    stack<int> stack1;
    stack<int> stack2;

    Queue() {
        // do intialization if necessary
    }

    void push(int element) {
        // write your code here
        stack1.push(element);
    }
    
    int pop() {
        // write your code here
        if (stack2.size() > 0) {
            int ret = stack2.top();
            stack2.pop();
            return ret;
        } else {
            while(stack1.size() > 0){
                stack2.push(stack1.top());
                stack1.pop();
            }
            return pop();
        }
    }

    int top() {
        // write your code here
        if (stack2.size() > 0)
            return stack2.top();
        else
             while(stack1.size() > 0){
                stack2.push(stack1.top());
                stack1.pop();
            }
        return stack2.top();
    }
};
