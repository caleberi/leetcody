class Solution {
public:
    // method 1
    // vector<int> singleNumber(vector<int>& nums) {
    //     unordered_map<int,int> num_to_freq;
    //     unordered_map<int,int> freq_to_num;
    //     for(int num:nums){
    //         if(num_to_freq.find(num)==num_to_freq.end())
    //             num_to_freq[num] = 1;
    //         else
    //             num_to_freq[num]++;
    //     }

    //     vector<int> ret;
    //     for (int num:nums){
    //         if(num_to_freq[num]==1){
    //            ret.push_back(num);
    //         }
    //     }

    //     return ret;
    // }
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> ret;
        sort(nums.begin(),nums.end());
        int i=0;
        for(;i<nums.size()-1;){
            int cur = nums[i];
            int pcr = nums[i+1];
            if ((pcr^cur)!=0){
                ret.push_back(nums[i]);
                i+=1;
                continue;
            }
            i+=2;
        }
        if(i==nums.size()-1){
            int cur = nums[i];
            int pcr = nums[i-1];
            if ((pcr^cur)!=0)
                ret.push_back(nums[i]);
        }
        return ret;
    }
};