# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        carry = 0
        while l1 and l2:
            temp = l1.val + l2.val + carry
            res.next = ListNode(val = temp % 10)
            carry = temp // 10
            l1, l2 = l1.next, l2.next
            res = res.next
        while l1:
            temp = l1.val + carry
            res.next = ListNode(val = temp % 10)
            carry = temp // 10
            l1 = l1.next
            res = res.next
        while l2:
            temp = l2.val + carry
            res.next = ListNode(val = temp % 10)
            carry = temp // 10
            l2 = l2.next
            res = res.next
        if carry: res.next = ListNode(val = carry)
        return dummy.next