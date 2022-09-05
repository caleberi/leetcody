package java_leetcode.com.leetcode;

import java.util.ArrayList;

public class PathWithMinimumEffort {
    public int minimumEffortPath(int[][] heights) {
        return 0; 
    }

    private ArrayList<ArrayList<Integer>> getNeighbours(int[][] heights, int x,int y){
        ArrayList<ArrayList<Integer>> neighbours =  new ArrayList<>();
        if (outOfBounds(heights, x-1, y)) {
            ArrayList<Integer> point = new ArrayList<>(); // up
            point.add(x-1);
            point.add(y);
            neighbours.add(point);
        }

        if (outOfBounds(heights, x+1, y)) { // down
            ArrayList<Integer> point = new ArrayList<>();
            point.add(x+1);
            point.add(y);
            neighbours.add(point);
        }

        if (outOfBounds(heights, x, y-1)) { // left
            ArrayList<Integer> point = new ArrayList<>();
            point.add(x+1);
            point.add(y);
            neighbours.add(point);
        }

        if (outOfBounds(heights, x, y+1)) { // right
            ArrayList<Integer> point = new ArrayList<>();
            point.add(x+1);
            point.add(y);
            neighbours.add(point);
        }
        return neighbours;
    }

    private boolean outOfBounds(int[][] heights,int x ,int y){
        return (x < 0 && x > heights.length-1) || (y < 0 && y > heights.length);
    }
}

