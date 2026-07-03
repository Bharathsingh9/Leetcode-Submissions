# Last updated: 7/3/2026, 12:48:02 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        fake = ListNode(0)
        fake.next = head
        pre = fake
        curr = head
        
        while curr is not None:
            while curr.next is not None and pre.next.val == curr.next.val:
                curr = curr.next
            
            if pre.next == curr:
                pre = pre.next
            else:
                pre.next = curr.next
                
            curr = curr.next
            
        return fake.next