#include <iostream>
#include <cstddef>

 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int minDiffInBST(TreeNode* root) {
        signed int  minDistance = 100000;
        minDiffInBSTHelper(root, &minDistance);
        return minDistance;
    }

    void minDiffInBSTHelper(TreeNode* parent,TreeNode* root, int* minDistance){
        if (root == nullptr )
            return;
        int diff = abs(parent->val - root->val);
        *minDistance = min(diff,*minDistance);
        if (root->left != nullptr)
            this->minDiffInBSTHelper(root,root->left,minDistance);
        if (root->right != nullptr)
            this->minDiffInBSTHelper(root,root->right,minDistance);
    }
};