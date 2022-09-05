package java_leetcode.com.leetcode;

public class ValidPalindrome {
    public boolean validPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while( i < j){
            if ( s.charAt(i) != s.charAt(j) ){
                return checkPalindrome(s,i,j-1) || checkPalindrome(s,i+1,j);
            }
           i += 1;
           j -= 1; 
        }
        return true;
       
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
    
}
