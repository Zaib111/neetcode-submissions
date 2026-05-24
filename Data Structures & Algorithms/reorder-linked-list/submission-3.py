# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # looking like a two-pointer problem, but we can't go backwards since this is a singly linked list
        # but, we can actually just find the midpoint of the list and reverse the second half to then use two pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = prev = None
        # now that we've found the midpoint of the list, we just reverse this half
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
         # using two-pointers approach now
        l, r = head, prev
        while r:
            l_next = l.next
            r_next = r.next
            l.next = r
            r.next = l_next
            l = l_next
            r = r_next