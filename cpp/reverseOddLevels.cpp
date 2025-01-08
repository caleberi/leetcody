#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;



struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* reverseOddLevels(TreeNode* root) {
        if (root == nullptr) return root;
        queue<TreeNode*> q;
        int level = 0;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            vector<TreeNode*> currentLevel;

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (level % 2 == 1) {
                    currentLevel.push_back(node);
                }
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }


            if (level % 2 == 1) {
                int left = 0, right = currentLevel.size() - 1;
                while (left < right) {
                    swap(currentLevel[left]->val, currentLevel[right]->val);
                    left++;
                    right--;
                }
            }

            currentLevel.clear();
            level++;
        }
        return root;
    }

    TreeNode* reverseOddLevels(TreeNode* root) {
        this->reverseOddLevelHelper(root->left, root->right, 0);
        return root;
    }

    void reverseOddLevelHelper(TreeNode* leftChild, TreeNode* rightChild, int level) {
        if (leftChild == nullptr || rightChild == nullptr) return;
        if (level % 2 == 0) {
            swap(leftChild->val, rightChild->val);
        }
        this->reverseOddLevelHelper(leftChild->left, rightChild->right, level + 1);
        this->reverseOddLevelHelper(leftChild->right, rightChild->left, level + 1);
    }
};