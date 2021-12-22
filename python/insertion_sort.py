def insertionSortList(head):
    current_node = head
    while current_node is not None:
        node_to_compare = current_node # 6
        while node_to_compare is not None: 
            if node_to_compare.val < current_node:
                detach_node()
                node_to_compare=node_to_compare.next
            else:
                break
        current_node = current_node.next

def swap_node(node_a,node_b):
    pass

def detach_node(prev,node):
    temp = node
    if node.next:
        prev.next = node.next.next
    temp.next = None
    return node