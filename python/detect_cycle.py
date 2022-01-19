from ast import Not


def detectCycle(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    if head.next.next == head:
        return head
    s = head.next
    f = head.next.next
    while f and f.next and s != f:
        s = s.next
        f = f.next.next
    if f is None or f.next is None:
        return None
    else:
        s = head
        while s != f:
            s = s.next
            f = f.next
        return s
