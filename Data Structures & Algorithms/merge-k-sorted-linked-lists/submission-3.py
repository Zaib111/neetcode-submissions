# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        # elif len(lists) == 1: return lists[0]
        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i - 1])
        return lists[-1]

    def mergeTwoLists(self, list1, list2):
        res = ListNode()
        dummy = res
        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        res.next = list1 if list1 else list2
        return dummy.next