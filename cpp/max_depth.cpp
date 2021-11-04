#include <cstdlib>
#include <algorithm>
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
    int maxDepth(TreeNode* root) {
        if(root==NULL){
            return 0;
        }
        return this->maxDepthHelper(root,0);
    }
    
    int maxDepthHelper(TreeNode* root,int height){
        if(root==NULL){
            return height;
        }
        
        int left_height = this->maxDepthHelper(root->left,height+1);
        int right_height = this->maxDepthHelper(root->right,height+1);
        return std::max(left_height,right_height);
    }
};