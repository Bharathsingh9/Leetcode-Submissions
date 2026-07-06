# Last updated: 7/6/2026, 11:41:51 AM
1class Solution:
2    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
3        # 1. Handle edge cases
4        if not head or not head.next:
5            return head
6        length = 0
7        count = head
8        while count.next:
9            length += 1
10            count = count.next
11        length += 1
12        k = k % length
13        p = head
14        for _ in range(length - k - 1):
15            p = p.next
16        count.next = head
17        head = p.next
18        p.next = None
19        return head