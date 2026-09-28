# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        while len(lists) > 1:
            l1, l2 = lists.pop(0), lists.pop(0)
            merged = self.mergeTwoLists(l1, l2)
            lists.append(merged)
        
        return lists[0] if lists else None
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2

        return dummy.next