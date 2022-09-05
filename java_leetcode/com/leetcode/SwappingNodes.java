package java_leetcode.com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class SwappingNodes {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public ListNode swapNodes(ListNode head, int k) {
        ListNode oneFromkthNodeFromFront = null;
        ListNode oneFromkthNodeFromBack = null;
        List<ListNode> list = new ArrayList<>();
        ListNode curr = head;
        while (head != null){
            list.add(curr);
            curr =  curr.next;
        }
        if(list.size()<2){
            return head;
        }
        oneFromkthNodeFromBack = list.get(list.size()-k-1);
        oneFromkthNodeFromFront = list.get(k-1);
        ListNode s1 = oneFromkthNodeFromFront.next;
        ListNode s2 = oneFromkthNodeFromBack.next;
        ListNode n1 = oneFromkthNodeFromFront.next.next;
        ListNode n2 = oneFromkthNodeFromBack.next.next;
        oneFromkthNodeFromBack.next = s1;
        oneFromkthNodeFromFront.next= s2;
        s1.next = n2;
        s2.next = n1;
        return head;
    }
}
