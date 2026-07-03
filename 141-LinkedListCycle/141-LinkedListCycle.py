# Last updated: 7/3/2026, 12:47:50 PM
class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True

    return False