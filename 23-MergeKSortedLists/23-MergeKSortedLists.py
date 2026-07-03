# Last updated: 7/3/2026, 12:48:43 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for i in lists:
            if i:
                heapq.heappush(heap, (i.val, id(i), i))
        dummy = ListNode(0)
        current = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
        
        return dummy.next
            