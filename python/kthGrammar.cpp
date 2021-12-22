#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int kthGrammar(int n, int k) {
        vector<string> tmp{"0"};
        for(int i = 1;i<n;i++){
            string new_gen = this->form_grammar_at_ith(tmp[i-1]);
            cout << "new_gen: " << new_gen << endl;
            tmp.push_back(new_gen);
        }
        return 0;
    }
    string form_grammar_at_ith(string prev)
    {
        string ret ="";
        int i = 0;
        for(;i<prev.length();i++){
            char curr = prev[i];
            if(curr=='0')
                ret+="01";
            else
                ret+="10";
        }
        return ret;
    }
};