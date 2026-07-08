# Last updated: 7/8/2026, 11:15:24 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
8        less_head = less_tail = ListNode(0)
9        greater_head = greater_tail = ListNode(0)
10    
11        while head:
12            if head.val < x:
13                less_tail.next = head
14                less_tail = less_tail.next
15            else:
16                greater_tail.next = head
17                greater_tail = greater_tail.next
18            head = head.next
19    
20        greater_tail.next = None
21        less_tail.next = greater_head.next
22    
23        return less_head.next