# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(next=head)
        counter = 0
        cur = head
        while counter < n:
            cur = cur.next
            counter += 1
        
        temp = head
        while cur.next:
            temp, cur = temp.next, cur.next
        
        temp.next = temp.next.next
        return head.next