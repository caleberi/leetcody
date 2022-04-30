package java_leetcode.com.leetcode;

import java.util.HashMap;

public class RomanToDecimal {
    public int romanToInt(String s) {
        HashMap<Character,Integer> symbolTable = new HashMap<Character,Integer>(){
            {
                put('I', 1);
                put('V', 5);
                put('X', 10);
                put('L', 50);
                put('C', 100);
                put('D', 500);
                put('M', 1000);
            }
        };

        int res = 0;
        for (int idx = 0; idx < s.length(); idx++) {
            if( idx+1 < s.length() && symbolTable.get(s.charAt(idx)) < symbolTable.get(s.charAt(idx+1))){
                res -= symbolTable.get(s.charAt(idx));
            }else{
                res += symbolTable.get(s.charAt(idx));
            }
        }
        return res;
    }
}
