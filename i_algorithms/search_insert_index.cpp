#include <vector>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if(target>nums.back())
             return nums.size();
        if(target<nums[0] && target<nums.back())
            return  0;
        int left = 0;
        int right = nums.size() - 1;
        int pivot;
        while (left <= right)
        {
            pivot = (left + (right - left) / 2);
            if (nums[pivot] == target)
                return pivot;
            if (target < nums[pivot]){
                if(pivot >=0 && nums[pivot-1]<target){
                    return pivot;
                }
                right = pivot - 1;
            }
            else{
                if(pivot <= nums.size()-2  && nums[pivot+1]>target){
                    if(nums[pivot+1]>target)
                        return pivot+1;
                    if(target<nums[pivot]&&target<nums.back()){
                        return nums.size()-1;
                    }
                    return pivot;
                } 
                left = pivot + 1;
            }
        }
        
        return -1;
    }
};