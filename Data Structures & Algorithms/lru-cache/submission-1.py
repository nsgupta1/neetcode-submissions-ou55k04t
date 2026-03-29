class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.store = defaultdict(Node)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        curr = self.store[key]
        self.removeNode(curr)
        self.addNode(curr)
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            curr = self.store[key]
            curr.val = value
            self.removeNode(curr)
            self.addNode(curr)
        else:
            curr = Node(key, value, None, None)
            self.addNode(curr)
        if len(self.store) > self.capacity:
            self.removeNode(self.tail.prev)

    def addNode(self, curr: Node) -> None:
        nextNode = self.head.next
        self.head.next = curr
        curr.prev = self.head
        nextNode.prev = curr 
        curr.next = nextNode
        self.store[curr.key] = curr

    def removeNode(self, curr:Node) -> None:
        if curr.next : 
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next
        self.store.pop(curr.key, None)

class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next