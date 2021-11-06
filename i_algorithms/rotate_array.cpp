class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k>nums.size()? k%nums.size():k;
        int t = nums.size()-k ;
        int i = t;
        vector<int> ret;
        for(;i<nums.size();i++){
            ret.push_back(nums[i]);
        }
        int j = 0;
        for(;j<t;j++){
            ret.push_back(nums[j]);
        }
        for(int x=0;x<ret.size();x++){
            nums[x]=ret[x];
        }
    }
};