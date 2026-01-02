# https://leetcode.com/problems/lru-cache/description/

# note that not abstracting the "refresh" method speeds this up a lot, I guess function call overhead not worth it for this problem

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(None, -1)
        self.tail = Node(None, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.refresh(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.mp:
            if len(self.mp) == self.cap:
                evict = self.tail.prev
                del self.mp[evict.key]
                evict.prev.next = self.tail
                self.tail.prev = evict.prev
            
            node = Node(key, value)
            self.mp[key] = node

            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
        else:
            node = self.mp[key]
            node.val = value

            self.refresh(node)
    
    def refresh(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)