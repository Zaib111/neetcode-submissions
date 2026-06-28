class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
         self.capacity = capacity
         self.map = {}

         self.left, self.right = Node(0,0), Node(0, 0)
         self.left.next, self.right.prev = self.right, self.left
        
    # remove from list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # insert at right
    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            node.val = value
        else:
            node = Node(key, value)
        self.insert(node)
        self.map[key] = node
        if len(self.map) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]