# Last updated: 7/6/2026, 11:42:59 AM
1class Solution:
2    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
3        dummy = ListNode(0, head)
4        prev, cur = dummy, head
5
6        while cur and cur.next:
7            npn = cur.next.next
8            second = cur.next
9
10            second.next = cur
11            cur.next = npn
12            prev.next = second
13
14            prev = cur
15            cur = npn
16        
17        return dummy.next