# Last updated: 7/3/2026, 12:48:00 PM
class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    curr = head

    while curr:
      while curr.next and curr.val == curr.next.val:
        curr.next = curr.next.next
      curr = curr.next

    return head