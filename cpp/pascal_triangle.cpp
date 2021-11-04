#include <vector>
using namespace std;
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if(rowIndex==0)
            return {1};
        if(rowIndex==1)
            return {1,1};
        vector<int> ret={};
        ret.push_back(1);
        vector<int> temp=getRow(rowIndex-1);
        int i=1;
        for(;i<temp.size();i++){
            ret.push_back(temp[i-1]+temp[i]);
        }
        ret.push_back(1);
        return ret;
    }
};