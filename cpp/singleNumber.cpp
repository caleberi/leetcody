class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
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
            if(num_to_freq[num]==1){
               ret.push_back(num);
            }
        }

        return ret;
    }
};