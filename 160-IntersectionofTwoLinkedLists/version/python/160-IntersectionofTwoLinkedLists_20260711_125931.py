# Last updated: 7/11/2026, 12:59:31 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
9        a, b = headA, headB
10        
11        while a != b:
12            a = a.next if a else headB
13            b = b.next if b else headA
14            
15        return a