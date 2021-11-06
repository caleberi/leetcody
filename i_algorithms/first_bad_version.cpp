// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
       int start=1;
       int end=n;
       int mid;
       while(start<=end){
           mid = start+((end-start)/2);
           if (isBadVersion(mid) && !isBadVersion(mid-1))
               return mid;
           if(isBadVersion(mid) && isBadVersion(mid-1)){
               end = mid-1;
           }else{
               start = mid+1;
           }
       }
       return 0;
    }
};