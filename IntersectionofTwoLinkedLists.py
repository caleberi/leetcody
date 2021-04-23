class Solution:
    def gl(self, head) -> int:
        i = 0
        c = head
        while c:
            i += 1
            c = c.next
        return i

    def md(self, head, d):
        i = 0
        c = head
        while c:
            if i == d:
                return c
            i += 1
            c = c.next
        return None

    def findIntersection(self, sa, sb):
        while sa and sb:
            if sa == sb:
                return sa
            sa = sa.next
            sb = sb.next
        return None

    def getIntersectionNode(self, ha: ListNode, hb: ListNode) -> ListNode:
        la = self.gl(ha)
        lb = self.gl(hb)
        if la > lb:
            sa = self.md(ha, la-lb)
            if sa is None:
                return None
            return self.findIntersection(sa, hb)
        elif lb > la:
            sb = self.md(hb, lb-la)
            if sb is None:
                return None
            return self.findIntersection(ha, sb)
        else:
            return self.findIntersection(ha, hb)
