class ListNode:

    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyToNode = {}

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def del_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self,node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def moveToHead(self,node):
        self.del_node(node)
        self.addToHead(node)

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        node = self.keyToNode[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.keyToNode:
            toAdd = ListNode(key,value,None,None)
            self.addToHead(toAdd)
            self.keyToNode[key] = toAdd
            if len(self.keyToNode) > self.cap:
                toDel = self.tail.prev
                del self.keyToNode[toDel.key]
                self.del_node(toDel)
        else:
            self.keyToNode[key].val = value
            self.moveToHead(self.keyToNode[key])

