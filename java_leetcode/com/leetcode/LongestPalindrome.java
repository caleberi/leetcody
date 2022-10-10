package java_leetcode.com.leetcode;

public class LongestPalindrome{
    public String longestPalindrome(String s) {
        String maxLengthSofar = "";
        for (int i = 0; i < s.length(); i++) {
            int j = i;
            int k = i;

            
            while (j >=0 && k < s.length() && s.charAt(j) == s.charAt(k)){
                j -= 1;
                k += 1;  
            }
            String temp = s.substring(j+1,k);
            maxLengthSofar = maxLengthSofar.length() >= temp.length() ? maxLengthSofar : temp;
            
            j = i;
            k = i+1;
            
            while (j >=0 && k < s.length() && s.charAt(j) == s.charAt(k)){
                j -= 1;
                k += 1;  
            }
                       
            temp = s.substring(j+1,k);
            maxLengthSofar = maxLengthSofar.length() >= temp.length() ? maxLengthSofar : temp;
            
        }
        return maxLengthSofar;
    }

    public static void main(String[] args) {
        LongestPalindrome longestPalindrome =  new LongestPalindrome();
        System.out.println(longestPalindrome.longestPalindrome("babad"));
    }
}