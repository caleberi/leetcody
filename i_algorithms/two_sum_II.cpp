#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for(int i=0;i<numbers.size();i++){
            int diff = target-numbers[i];
            int found = search(numbers,diff,i);
            if(found!=-1){
                return {i+1,found+1};
            }
        }
        return {};
    }
    
    int search(vector<int> &nums, int target,int i)
    {
        int left = 0;
        int right = nums.size() - 1;
        int pivot;
        while (left <= right)
        {
            pivot = (left + (right - left) / 2);
            if (nums[pivot] == target&&pivot!=i)
                return pivot;
            if (nums[pivot] > target)
                right = pivot - 1;
            else
                left = pivot + 1;
        }
        return -1;
    }
};