class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key, self.val = key, val
        self.next, self.prev = next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
        self.insert(node)
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def insert(self, cur):
        current_last = self.right.prev
        current_last.next = cur
        cur.prev = current_last
        cur.next = self.right
        self.right.prev = cur

    def remove(self, cur):
        cur.prev.next = cur.next
        cur.next.prev = cur.prev