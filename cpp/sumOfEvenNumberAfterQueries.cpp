#include <vector>

using namespace std;

class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        
        vector<int> ret;
        int ns = nums.size();
        int qs = queries.size();
        
        int total = 0;
        
        for(int eptr = 0 ; eptr < ns ; eptr++)
            if (nums[eptr]%2==0)
                total += nums[eptr];
    
        
        for (int idx = 0;idx < qs ;idx++){
            int val = queries[idx][0];
            int i = queries[idx][1];
            
            int newVal = nums[i] + val;
            
            if (nums[i]%2==0)
                total -= nums[i];
            if (newVal %2 == 0)
                total += newVal;
              
            nums[i] = newVal;
            
            ret.push_back(total);
        }
        
        return ret; 
    };

};