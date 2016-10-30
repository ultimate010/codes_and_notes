/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/count-of-smaller-number
@Language: C++
@Datetime: 16-07-06 10:36
*/

class SegmentTree {
public:
    SegmentTree * left;
    SegmentTree * right;
    int start;
    int end;
    int count;
    
    SegmentTree(int _start, int _end) {
        start = _start; end = _end;
        left = right = NULL;
        count = 0;
    }
    
    static SegmentTree * buildTree(int start, int end) {
        if (start > end) return NULL;
        SegmentTree * root = new SegmentTree(start, end);
        if (start != end) {
            int mid = ((end - start) >> 1) + start;
            root->left = SegmentTree::buildTree(start, mid);
            root->right = SegmentTree::buildTree(mid + 1, end);
        }
        return root;
    }
    
    void inc(int a) {
        if (start == a && end == a) {
            count += 1;
            return ;
        }
        int mid = ((end - start) >> 1) + start;
        if (mid >= a)
            left->inc(a);
        else
            right->inc(a);
        count = left->count + right->count;
    }
    
    int sum(int _start, int _end) {
        if (start > _end || end < _start) {
            return 0;
        }
        if (start >= _start && end <= _end) {
            return count;
        }
        return left->sum(_start, _end) + right->sum(_start, _end);
    }
    
    ~SegmentTree() {
        if (left) 
            delete left;
        if (right) 
            delete right;
    }
};


class Solution {
public:
   /**
     * @param A: An integer array
     * @return: The number of element in the array that 
     *          are smaller that the given integer
     */
    vector<int> countOfSmallerNumber(vector<int> &A, vector<int> &queries) {
        // write your code here
        int m = A.size();
        int n = queries.size();
        vector<int> ret(n, 0);
        if (m == 0)
            return ret;
        int mm = INT_MIN;
        for (auto n : A) {
            mm = max(mm, n);
        }
        
        SegmentTree * root = SegmentTree::buildTree(0, mm);
        for (auto n : A) {
            root->inc(n);
        }
        for (int i = 0; i < n; i++ ) { 
            ret[i] = root->sum(0, queries[i] - 1);
        }
        return ret;
    }
};

