#include  <unordered_map>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

struct Node;
struct Graph;


struct Node {
    int value;
    unordered_map<int,Node* > in_contact_with;

    Node(int value){
       this->value = value;
    }

    void connect(Node* const node) {
        unordered_map<int, Node*>::iterator found = 
        find(in_contact_with.begin(),in_contact_with.end(),node->value);
        if(found!=in_contact_with.end())
            return;
        in_contact_with.insert(make_pair(node->value,node));
    }

    void disconnect( const Node* node){
        in_contact_with.erase(node->value);
    }
     
    ~Node(){

        for(auto itr=in_contact_with.begin();itr!=in_contact_with.end();itr++){
            Node* entry = itr->second;
            if (entry!=NULL){
                delete entry;
                in_contact_with.erase(itr->first);
                return;
            }
            in_contact_with.erase(itr->first);
        }
        
    }

};

struct Graph{
    unordered_map<int, Node*> node_map;
    Graph(){}
    ~Graph(){}
    void add_to_graph( Node* const node) {
        unordered_map<int, Node*>::iterator found = 
        find(node_map.begin(),node_map.end(),node->value);
        if(found!=node_map.end()&&found->first!=NULL)
            return;
        node_map.insert(make_pair(node->value,node));
    }
};

int celebrity_gossip(vector<vector<int>>& celebrity_gossips) {
    Graph graph = Graph();
    for(int i = 0; i < celebrity_gossips.size();i++){
        Node* node = new Node(i+1);
        for (int j=0;j<celebrity_gossips[i].size();j++){
            Node* child = new Node(celebrity_gossips[i][j]);
            node->connect(child);
            graph.add_to_graph(node);
        }
        graph.add_to_graph(node);
    }
    for(auto node : graph.node_map){
        if(node.second==NULL)
            return node.first;
    }

    return -1 ;
};

int get_celebrity(vector<vector<int>>& gossips){
    if (gossips.size()==0)
        return -1;
    return celebrity_gossip(gossips);
}

int main() {
    vector<vector<int>> gossips({{1,3},{2,3}});
    cout << get_celebrity(gossips) << endl;
}