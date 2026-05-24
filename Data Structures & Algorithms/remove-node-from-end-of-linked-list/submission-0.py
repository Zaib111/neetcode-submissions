# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer approach with l and r pointers to find where n is located
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # setting right pointer
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # finding where the right pointer is now (where n is)
        while right:
            right = right.next
            left = left.next
        # left will be one behind n now so that it can move its pointer
        left.next = left.next.next

        return dummy.next