#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public: 
    /**
     * @brief function to mutliply two numbers.
     * this is not an optimal solution as it can't be stored due to 
     * memory  size 
     * @param num1  string to be multiplied
     * @param num2 string to multipy with
     * @return string 
     */
    string multiply(string num1, string num2) {
        long long n1 = 0;
        long long p = 1;

        for(int i=num1.size()-1;i>=0;i--){
            n1+= (num1[i]-48)*p;
            p*=10;
        }
        
        long long n2=0;
        p = 1;

        for(int i=num2.size()-1;i>=0;i--){
            n2+= (num2[i]-48)*p;
            p*=10;
        }
        long long int  n = n2 * n1;
        return to_string(n);
    }
    
    string multiply_v2(string num1,string num2){
        if (num1.size()==0 || num2.size()==0){
            return "";
        } 
        vector<int> res(num1.size()+num2.size(),0);
        for (int i=num1.size()-1; i>=0;i--){
            for (int j=num2.size()-1;j>=0;j--){
                res[i+j+1] += (num2[i]-48) * (num1[i]-48);
                res[i+j] += res[i+j+1]/10;
                res[i+j+1] %= 10;   
            }
        }
        int i=0;
        string ans="";
        while (res[i] == 0) i++;
        while (i < res.size()) ans+=to_string(res[i++]);
        return ans;
    }
};