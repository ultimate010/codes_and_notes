/*
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/construct-binary-tree-from-preorder-and-inorder-traversal
@Language: C++
@Datetime: 16-08-05 08:48
*/

/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
 

class Solution {
    /**
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
public:
    typedef vector<int>::iterator iter;
    TreeNode *buildTree(iter pB, iter pE, iter iB, iter iE) {
        if (pB == pE)
            return NULL;
        TreeNode * root = new TreeNode(*iB);
        iter pM = find(pB, pE, *iB);
        root->left = buildTree(pB, pM, iB + 1, iB + 1 + (pM - pB));
        root->right = buildTree(pM + 1, pE, iB + 1 + (pM - pB), iE);
        return root;
    }
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        // write your code here
        return buildTree(inorder.begin(), inorder.end(),
        preorder.begin(), preorder.end());
    }
};