package java_leetcode.com.test;

import java.util.LinkedList;
import java.util.List;

public class SetTest{
    public static void main(String[] args) {
        List<String> data = new LinkedList<>();

        data.add("1");
        data.add("2");
        data.add("4");
        data.add("8");
        data.add("9");
        data.add("10");

        data.removeIf(i-> (i.equals("3")));

        System.out.println(data);

    }
}