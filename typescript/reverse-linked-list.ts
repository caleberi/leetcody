class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
};

function reverseList(head: ListNode | null): ListNode | null {
    if(head == null){
        return head
    }
    if (head.next === null){
        return head;
    }
    let prevNode = reverseList(head.next);
    head.next.next =  head;
    head.next =  null;
    return prevNode;
};