#include <unordered_map>
using namespace std;
class Solution {
public:
    
    int fib_helper(int n,unordered_map<int,int>& cache){
        if(cache.find(n)!=cache.end())
            return cache[n];
        if(n==0||n==1)
            return n;
        int t = this->fib_helper(n-1,cache)+ this->fib_helper(n-2,cache);
        if(cache.find(n)==cache.end())
            cache[n]=t;
        return t;
    }
    
    int fib(int n) {
        if(n<0)
            return n;
        unordered_map<int,int> cache;
        return this->fib_helper(n,cache);
    }
    
    
};