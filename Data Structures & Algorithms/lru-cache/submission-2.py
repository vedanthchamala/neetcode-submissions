class ListNode:
    def __init__(self, key, val):
        self.next = None
        self.val = val
        self.prev = None
        self.key = key



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.right.prev = self.left
        self.left.next = self.right
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val





    
    def remove(self, node):
        nxt = node.next 
        prv = node.prev
        nxt.prev = prv
        prv.next = nxt


    def insert(self, node):
        end = self.right.prev
        end.next = node
        node.prev = end
        node.next = self.right
        self.right.prev = node






        
