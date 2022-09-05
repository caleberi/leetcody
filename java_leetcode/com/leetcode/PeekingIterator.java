package java_leetcode.com.leetcode;

import java.util.Iterator;
import java.util.LinkedList;

// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

// 14 / 14 test cases passed.
// Status: Accepted
// Runtime: 8 ms
// Memory Usage: 43.7 MB

public class PeekingIterator implements Iterator<Integer> {
    private final Iterator<Integer> iterator;
    private  LinkedList<Integer> queue;
 	public PeekingIterator(Iterator<Integer> iterator) {
        this.iterator = iterator;
        this.queue =  new LinkedList<>();
        while(iterator.hasNext()){
             queue.add(iterator.next());
        }
    }
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return  queue.peekFirst();
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
        return queue.pollFirst();
	}
	
	@Override
	public boolean hasNext() {
	    return !queue.isEmpty();
	}
}