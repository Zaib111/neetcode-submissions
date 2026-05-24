# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        prev = ListNode()
        head = prev
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                node = ListNode(curr1.val)
                prev.next = node
                prev = prev.next
                curr1 = curr1.next
            else:
                node = ListNode(curr2.val)
                prev.next = node
                prev = prev.next
                curr2 = curr2.next
        if curr1:
            prev.next = curr1
        else:
            prev.next = curr2
        return head.next
