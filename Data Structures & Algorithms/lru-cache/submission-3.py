class ListNode:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
        self.res = {} # map from key to node

    def get(self, key: int) -> int:
        if key in self.res:
            # want to move this key value pair to the end of the list
            node = self.res[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.res:
            node = self.res[key]
            self.remove(node)
            node.val = value
            self.insert(node)
        else:
            new_node = ListNode(key, value)
            self.res[key] = new_node
            self.insert(new_node)

            if len(self.res) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.res[lru.key]
    
    def insert(self, cur):
        current_last = self.right.prev
        current_last.next = cur
        cur.prev = current_last
        cur.next = self.right
        self.right.prev = cur
    
    def remove(self, cur):
        prev, nxt = cur.prev, cur.next
        prev.next, nxt.prev = nxt, prev