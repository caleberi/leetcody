
#include <iostream>
#include <cstddef>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>   

using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* createNewNode(int val){
        return new Node(val);
    }
    Node* copyRandomList(Node* head) {
        Node* original_itr = head;
        map<Node*,Node*> mp;
        while (original_itr!=nullptr){
            Node* cnode = createNewNode(original_itr->val);
            mp[original_itr] = cnode; 
            original_itr= original_itr->next;
        }

        original_itr = head;
        while (original_itr != nullptr){
            mp[original_itr]->next= mp[original_itr->next];
            mp[original_itr]->random = mp[original_itr->random];
             original_itr= original_itr->next;
        }
        return mp[head];
    }
};