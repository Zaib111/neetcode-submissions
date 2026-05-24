# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        left = head

        # reverse right half
        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt
        right = prev
        # populate left half
        while right:
            right_next = right.next
            right.next = left.next
            left.next = right
            right = right_next
            left = left.next.next