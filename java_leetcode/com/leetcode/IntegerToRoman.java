package java_leetcode.com.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class IntegerToRoman {
    public String intToRoman(int num) {
        String[] thousands = new String[]{"","M","MM","MMM"};
        String[] hundreds =  new String[]{"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        String[] tens =  new String[]{"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        String[] units =  new String[]{"","I","II","III","IV","V","VI","VII","VIII","IX"};

        return thousands[num/1000]+hundreds[(num%1000)/100]+tens[((num%1000)%100)/10] + units[((num%1000)%100)%10];
        
    }
}

/**
 * 
 * 1994
 * 
 */