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
            slow, fast = slow.next, fast.next.next
        
        # reverse from midpoint
        prev, curr = None, slow.next
        slow.next = prev
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # form new list
        tail = prev
        curr = head
        while tail:
            tail_left = tail.next
            head_right = curr.next
            curr.next = tail
            tail.next = head_right
            curr = head_right
            tail = tail_left