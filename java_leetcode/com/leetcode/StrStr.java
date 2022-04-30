package java_leetcode.com.leetcode;

public class StrStr {
    public int strStr(String haystack, String needle) {
        if (needle.length()==0){
            return 0;
        }
        if (needle.length()>haystack.length()){
            return -1;
        }
        for(int i=0;i<haystack.length();i++){
            if(haystack.charAt(i)==needle.charAt(0)){
                if(haystack.substring(i,i+needle.length()).equals(needle))
                    return i;
            }
        }
        return -1;
    }
    // public int strStr(String haystack, String needle) {
    //     if (needle.length()==0){
    //         return 0;
    //     }
    //     if (needle.length()>haystack.length()){
    //         return -1;
    //     }
    //     return  haystack.indexOf(needle);
    // }
    public static void main(String[] args) {
        StrStr test =  new StrStr();
        System.out.println(test.strStr("haystack", "stack"));
    }
}
