# Last updated: 7/3/2026, 12:47:31 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        current=head
        l=[]
        while current:
            l.append(current.val)
            current=current.next
        return l==l[::-1]
        