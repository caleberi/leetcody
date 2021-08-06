class Solution
{
public:
    //      bool helper(string str,int first,int last){
    // if(str.length()==1) return false;
    // 	if(first==last)return true;
    // 	if(first>last)return true;
    // 	if(str[first]==str[last]) return helper(str,first+1,last-1);
    // 	return false;
    // }
    // bool helper(string str) {
    // if(str.length()==1) return false;
    //   for(int i=0,j=str.length()-1;i<=j;++i,--j){
    // 		if(str[i]!=str[j])return false;
    // 	}
    //   return true;
    // }

    bool helper(string str)
    {

        for (string::iterator itr_beg = str.begin(), itr_end = str.end() - 1; itr_beg <= itr_end; itr_beg++, itr_end--)
        {
            if (*itr_beg != *itr_end)
                return false;
        }
        return true;
    }

    bool isPalindrome(int x)
    {

        string s = to_string(x);
        return helper(s);
    }
};