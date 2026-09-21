# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        cur1, cur2 = list1, list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                temp.next = cur1
                cur1 = cur1.next
                temp = temp.next
            else:
                temp.next = cur2
                cur2 = cur2.next
                temp = temp.next
        
        if cur1:
            temp.next = cur1
        else:
            temp.next = cur2
        

        return head.next