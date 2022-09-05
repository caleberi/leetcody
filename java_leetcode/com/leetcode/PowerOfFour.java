package java_leetcode.com.leetcode;

public class PowerOfFour {
    public boolean isPowerOfFour(int n) {
        if (n<0)
            return false;
        int remainder = n % 4;
        if (remainder>0)
            return isPowerOfFour(remainder);
        return true;
    }
}
