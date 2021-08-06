class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return self.getDecimalValueHelper(head)[0]

    def getDecimalValueHelper(self, head: ListNode) -> int:
        if head is None:
            return (0, 0)

        total, exp = self.getDecimalValueHelper(head.next)
        currbit = head.val
        total += currbit * (2**exp)
        return (total, exp+1)
