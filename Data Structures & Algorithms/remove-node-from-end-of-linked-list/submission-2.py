# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the list in one pass, then just do another pass and iterate n-1 times
        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next
        # curr = head
        # counter = 0
        # i = length - n + 1
        # if i == 1:
        #     return head.next
        # while curr:
        #     counter += 1
        #     if counter == i - 1:
        #         curr.next = curr.next.next
        #     curr = curr.next
        # return head
        dummy = ListNode(0, head)
        a, b = dummy, head
        counter = 0
        while counter < n:
            b = b.next
            counter += 1
        while b:
            b = b.next
            a = a.next
        a.next = a.next.next
        return dummy.next