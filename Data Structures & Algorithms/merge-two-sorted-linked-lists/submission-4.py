# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val > curr2.val:
                tail.next = curr2
                curr2 = curr2.next
            else:
                tail.next = curr1
                curr1 = curr1.next
            tail = tail.next
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2
        return dummy.next