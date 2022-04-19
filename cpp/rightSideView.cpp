 #include <cstddef>
 #include <iostream>
 #include <vector>
 #include <deque>

 using namespace std;

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
    vector<int> rightSideView(TreeNode* root) {
        return this->rightSideViewHelper(root);
    }

    vector<int> rightSideViewHelper(TreeNode* root){
        if (root == nullptr)
            return {};
        deque<TreeNode*> queue;
        queue.push_back(root);
        vector<int> ret;
        while(queue.size()){
            int size(queue.size());
            int i(0);
            while(i<size){
                TreeNode* curr = queue.front();
                if(i==size-1){
                    ret.push_back(curr->val);
                }
                if (curr->left != nullptr)
                queue.push_back(curr->left);
                if(curr->right !=nullptr)
                    queue.push_back(curr->right);
                queue.pop_front();
                i++; 
            }
        }
        return ret;
    }
};