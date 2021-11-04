#include <unordered_map>
using namespace std;

class Solution {
public:
    int climbStairsHelper(int n,unordered_map<int,int>& cache) {
        if(cache.find(n)!=cache.end())
            return cache[n];
        if(n==0)
            return 1;
        if(n==1)
            return 1;
        if(n==2)
            return 2;
        int t = this->climbStairsHelper(n-1,cache)+ this->climbStairsHelper(n-2,cache);
        if(cache.find(n)==cache.end())
            cache[n]=t;
        return t;
    }
    int climbStairs(int n){
        if(n<0)
            return n;
        unordered_map<int,int> cache;
        return this->climbStairsHelper(n,cache);
    }
};