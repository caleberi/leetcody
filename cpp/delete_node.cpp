#include <cstddef>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}};
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode* nodeToDelete = this->searchForNode(root,key);
        if(searchForNode==nullptr)
            return root;
        TreeNode* replacementNode = this->findReplacementNode(nodeToDelete);
        this->swapTreeNode(nodeToDelete,replacementNode);
        nodeToDelete = nullptr;
        return root;
    }

    void swapTreeNode(TreeNode* treeOne,TreeNode* treeTwo){
        TreeNode* temp1 = treeOne;
        TreeNode* temp2 = treeOne;
        treeTwo->val = temp1->val;
        treeTwo->left = temp1->left;
        treeTwo->right= temp1->right;
        treeOne->val = temp2->val;
        treeOne->left = temp2->left;
        treeOne->right= temp2->right;
    }

    TreeNode* searchForNode(TreeNode* root,int key){
        if(root!=nullptr){
            if(root->val==key){
                return root;
            }
            if(root->val > key){
                return this->searchForNode(root->left,key);
            }
            return this->searchForNode(root->right,key);
        }
        return nullptr;
    }

    // TreeNode* findReplacementNode(TreeNode* nodeToDelete){
    //     if(nodeToDelete->left!=nullptr || nodeToDelete->right!=nullptr){
    //         if(nodeToDelete->left!=nullptr && nodeToDelete->right==nullptr){
    //             no
    //         }
    //         else if(nodeToDelete->right!=nullptr && nodeToDelete->left==nullptr){
    //             this->findReplacementNode(
    //                 nodeToDelete->val < nodeToDelete->right->val ? 
    //                 nodeToDelete->right : nodeToDelete);
    //         }else
    //         {
    //             nodeToDelete = nullptr;
    //             return nodeToDelete;
    //         }
            
    //     }
    //     return nodeToDelete;
    // }
};