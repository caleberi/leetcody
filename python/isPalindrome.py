# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        return linkedListPalindrome(head)


def getLinkedListLength(head):
    count = 1
    while head is not None:
        count += 1
        head = head.next
    return count


def getMiddleNode(node, length):
    count = 1
    while count != length:
        count += 1
        node = node.next
    return node


def reverseLinkedList(node):
    prevNode = None
    currentNode = node
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    return prevNode


def linkedListPalindrome(head):
    length = getLinkedListLength(head)
    startNode = head
    middleEndNode = getMiddleNode(head, length//2)
    middleStartNode = reverseLinkedList(middleEndNode)
    middleEndNode.next = None
    while startNode is not None and middleStartNode is not None:
        if startNode.val != middleStartNode.val:
            return False
        startNode = startNode.next
        middleStartNode = middleStartNode.next
    return True
