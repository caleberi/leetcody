class Solution {
public:
    int arrangeCoins(int n) {
        return this->arrangeCoinsHelper(1,n);
    }
    int arrangeCoinsHelper(int r,int n){
        if (r>n)
            return r-1;
        n = n - r;
        r = r + 1;
        return this->arrangeCoinsHelper(r,n);
    }
};