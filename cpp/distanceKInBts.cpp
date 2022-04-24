#include <iostream>
#include <cstddef>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


// 57 / 57 test cases passed.
// Status: Accepted
// Runtime: 8 ms
// Memory Usage: 15.1 MB
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int> ret;
        map<TreeNode*,TreeNode*> history;
        this->dfs(history,root,nullptr);
        deque<TreeNode*> queue;
        queue.push_back(target);
        set<TreeNode*> seen;
        seen.insert(target);
        int dst = 0;
        while (queue.size()!=0 && dst<k)
        {
            int sz = queue.size();
            dst++;
            for (int i = 0; i < sz; i++)
            {
                TreeNode* curr = queue.front();
                queue.pop_front();
                if (curr->left != nullptr && seen.find(curr->left) == seen.end()){
                    queue.push_back(curr->left);
                    seen.insert(curr->left);
                }

                if (curr->right != nullptr && seen.find(curr->right) == seen.end()){
                    queue.push_back(curr->right);
                    seen.insert(curr->right);
                }

                TreeNode* parent = history[curr];
                if (parent!=nullptr && seen.find(parent) == seen.end()){
                    queue.push_back(parent);
                    seen.insert(parent);
                }   
                
            }
           
        }

        for_each(queue.begin(),queue.end(),[&ret,&queue](TreeNode* node){
            ret.push_back(node->val);
        });
        
        return ret;
    }
    void dfs(
        map<TreeNode*,TreeNode*>& history,
        TreeNode* node,
        TreeNode* parent){
        if (node != nullptr){
            history.insert(pair<TreeNode*,TreeNode*>(node,parent));
            this->dfs(history,node->left,node);
            this->dfs(history,node->right,node);
        }
    }
};