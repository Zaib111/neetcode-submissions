"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        curr = head
        res = Node(0)
        dummy = res

        while curr:
            val = curr.val
            nxt = curr.next
            copies[curr] = Node(val, nxt, Node(0))
            curr = curr.next
        curr = head
        while curr:
            res.next = copies[curr]
            if curr.random:
                res.next.random = copies[curr.random]
            else:
                res.next.random = None
            curr = curr.next
            res = res.next
        return dummy.next