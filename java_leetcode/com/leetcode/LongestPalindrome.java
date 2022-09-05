package java_leetcode.com.leetcode;

public class LongestPalindrome{
    public String longestPalindrome(String s) {
        String maxLengthSofar = "";
        for (int i = 0; i < s.length(); i++) {
            int j = i-1;
            int k = i+1;

            while( j > 0 && k < s.length()){
                if ( s.charAt(j) == s.charAt(k)){
                    j -= 1;
                    k += 1; 
                }else{
                    break;
                }
            }
            if (checkPalindrome(s,k,j)){
                String temp = s.substring(j+1,k);
                maxLengthSofar = maxLengthSofar.length() > temp.length() ? maxLengthSofar : temp;
            }
            
            System.out.println(maxLengthSofar);
            
        }
        return maxLengthSofar;
    }

    private boolean checkPalindrome(String s, int i, int j){
        while( i < j){
            if ( s.charAt(i) != s.charAt(j) ){
                return false;
            }
           i += 1;
           j -= 1; 
        }
        return true;
    }
    public static void main(String[] args) {
        LongestPalindrome longestPalindrome =  new LongestPalindrome();
        System.out.println(longestPalindrome.longestPalindrome("babad"));
    }
}