# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            add = total % 10
            carry = total // 10
            cur.next = ListNode(add)
            cur = cur.next
            l1, l2 = l1.next, l2.next
        while l1:
            total = l1.val + carry if carry else l1.val
            add = total % 10
            carry = total // 10
            cur.next = ListNode(add)
            cur = cur.next
            l1 = l1.next
        while l2:
            total = l2.val + carry if carry else l2.val
            add = total % 10
            carry = total // 10
            cur.next = ListNode(add)
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(carry)

        return dummy.next

        