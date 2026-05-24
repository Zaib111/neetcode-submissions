# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # two pointers one on left side one on right side
        l = head
        # finding midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reversing right side
        r, r_none = None, slow.next
        slow.next = None
        while r_none:
            nxt = r_none.next
            r_none.next = r
            r = r_none
            r_none = nxt
        # mutating list
        while l and r:
            after_l = l.next
            after_r = r.next
            l.next = r
            l.next.next = after_l
            r = after_r
            l = after_l