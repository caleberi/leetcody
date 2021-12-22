#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

template<typename T>
void print_vector(vector<T> vec){
    for(T v : vec){
        cout << v << "\n";
    }
    cout << endl;
}
template<typename T,typename U>
void print_map(unordered_map<T,U> map){
    for(auto entry : map){
        cout << entry.first << " <===> " << entry.second << " \n";
    }
    cout << endl;
}

class StackSort{
    public:
        vector<int> sort_stack(vector<int> stk){
            if (stk.size()==0)
                return stk;
            int top = stk.back();
            stk.pop_back();
            sort_stack(stk);
            this->insert_in_sorted_stack(stk,top);
            stk.push_back(top);
            return stk;
        }

        void insert_in_sorted_stack(vector<int> stk,int value){
            if(stk.size()==0 || stk.back()<= value){
                stk.push_back(value);
                return;
            }
            int top = stk.back();
            stk.pop_back();
            insert_in_sorted_stack(stk,value);
            stk.push_back(top);
        }
};


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> num_to_freq;
        unordered_map<int,int> freq_to_num;
        for(int num:nums){
            if(num_to_freq.find(num)==num_to_freq.end())
                num_to_freq[num] = 1;
            else
                num_to_freq[num]++;
        }

        vector<int> ret;
        for (int num:nums){
            freq_to_num[num_to_freq[num]] = num;
        }

        for(auto entry : freq_to_num){
            ret.push_back(entry.first);
        }
        StackSort stk;
        ret = stk.sort_stack(ret);
        vector<int> ans;
        int i;
        for(i=0;i<k;i++){
            ans.push_back(freq_to_num[ret.back()]);
            ret.pop_back();
        }
        return ans;
    }
}; 