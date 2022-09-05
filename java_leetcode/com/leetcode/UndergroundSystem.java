package java_leetcode.com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class UndergroundSystem {
    private final Map<String,Integer> checkIn; 
    private final Map<String,Integer> checkOut; 
    public UndergroundSystem() {
        checkIn = new HashMap<>();
        checkOut = new HashMap<>();
    }

    public void checkIn(int id, String stationName, int t) {
        String  key = stationName+":"+t;
        if(!checkIn.containsKey()){
            checkIn.put(stationName+":"+t,id );
        }
    }
    
    public void checkOut(int id, String stationName, int t) {
        if(!checkOut.containsKey(id)){
            checkOut.put(stationName+":"+t,id);
        }
    }
    
    public double getAverageTime(String startStation, String endStation) {
        Map.Entry<Integer,String> = checkIn.
    }
}
